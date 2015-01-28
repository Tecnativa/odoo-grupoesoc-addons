# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp.osv import fields, orm


class MailComposeForward(orm.TransientModel):
    """Allow forwarding a message.

    It duplicates the message and optionally attaches it to another object
    of the database and sends it to another recipients than the original one.
    """

    _name = "mail.compose.forward"
    _inherit = "mail.compose.message"

    _models = [
        "crm.lead",
        "crm.meeting",
        "crm.phonecall",
        "mail.group",
        "note.note",
        "product.product",
        "project.project",
        "project.task",
        "res.partner",
        "sale.order",
    ]

    def models(self, cr, uid, context=None):
        """Get allowed models and their names.

        It searches for the models on the database, so if modules are not
        installed, models will not be shown.
        """

        context = dict(context) if context else dict()
        model_pool = self.pool.get('ir.model')
        model_ids = model_pool.search(
            cr, uid,
            [('model', 'in', context.get("model_list", self._models))],
            order="name", context=context)
        model_objs = model_pool.browse(cr, uid, model_ids, context=context)
        return [(m.model, m.name) for m in model_objs]

    _columns = {
        "destination_object_id": fields.reference(
            "Destination object",
            selection=models,
            size=128,
            help="Object where the forwarded message will be attached"),
        "move_attachments": fields.boolean(
            "Move attachments",
            help="Attachments will be assigned to the chosen destination "
                 "object and you will be able to pick them from its "
                 "'Attachments' button, but they will not be there for "
                 "the current object if any. In any case you can always "
                 "open it from the message itself."),

        # Override static relation table names in mail.compose.message
        "partner_ids": fields.many2many(
            "res.partner",
            "mail_compose_forward_res_partner_rel",
            "wizard_id",
            "partner_id",
            "Additional Contacts"),
        "attachment_ids": fields.many2many(
            "ir.attachment",
            "mail_compose_forward_ir_attachments_rel",
            "wizard_id",
            "attachment_id",
            "Attachments"),
    }

    def default_get(self, cr, uid, fields, context=None):
        """Fix default values.

        Sometimes :meth:`openerp.addons.mail.mail_compose_message
        .mail_compose_message.default_get` overwrites the default value
        for the ``subject`` field, even when it gets the right default value
        from the context.

        This method fixes that by getting it from the context if available.
        """

        context = dict(context) if context else dict()

        result = super(MailComposeForward, self).default_get(
            cr, uid, fields, context)

        if "subject" in result and "default_subject" in context:
            result["subject"] = context["default_subject"]

        return result

    def onchange_destination_object_id(self, cr, uid, ids,
                                       destination_object_id, context=None):
        """Update some fields for the new message."""

        context = dict(context) if context else dict()
        model = res_id = res_name = False

        if destination_object_id:
            model, res_id = destination_object_id.split(",")
            res_id = int(res_id)

            context["model_list"] = context.get("model_list", [model])
            model_name = dict(self.models(cr, uid, context=context)).get(model)
            res_name = (self.pool.get(model)
                        .name_get(cr, uid, res_id, context=context)[0][1])
            if model_name:
                res_name = "%s %s" % (model_name, res_name)

        return {"value": {"model": model,
                          "res_id": res_id,
                          "record_name": res_name}}

    def send_mail(self, cr, uid, ids, context=None):
        """Send mail and execute the attachment relocation if needed."""

        # Let the parent do de hard work
        result = super(MailComposeForward, self).send_mail(
            cr, uid, ids, context=context)

        # Relocate attachments if needed
        att_pool = self.pool.get("ir.attachment")
        for wz in self.browse(cr, uid, ids, context=context):
            if (wz.move_attachments and
                    wz.model and
                    wz.res_id and
                    wz.attachment_ids):
                att_pool.write(
                    cr,
                    uid,
                    [att.id for att in wz.attachment_ids],
                    {"res_model": wz.model, "res_id": wz.res_id},
                    context=context)

        return result
