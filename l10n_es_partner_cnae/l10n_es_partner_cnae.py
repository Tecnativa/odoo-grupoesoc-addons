# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014  Grupo ESOC <www.grupoesoc.es>
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

class cnae_codes(orm.Model):
    """Store all CNAE codes."""

    _name = "l10n_es_partner_cnae.cnae_codes"
    _parent_store = True

    def _full_name(self, cr, uid, ids, field_name, arg, context=None):
        """Get CNAE code and name together."""

        result = {}
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = "%s - %s" % (obj.code, obj.description)

        return result

    def _recalculate(self, cr, uid, ids, context=None):
        """Recalculate all records changed in this model."""

        return ids

    _columns = {
        "code": fields.char("Code", required=True, size=5),
        "description": fields.char("Description", required=True, size=200),
        "name": fields.function(
            _full_name,
            readonly=True,
            string="CNAE Code and description",
            store={_name: (_recalculate, ["code", "description"], 10)},
            type="char"),
        "parent_id": fields.many2one(_name, "Parent CNAE"),
        "parent_left": fields.integer("Left parent"),
        "parent_right": fields.integer("Right parent"),
        "child_ids": fields.one2many(_name, "parent_id"),
    }

    _sql_constraints = [
        ("code_unique",
         "unique(code)",
         "CNAE codes must be unique"),
    ]

class l10n_es_partner_cnae(orm.Model):
    """Add CNAE field to all partners.

    A parnter can only have one of the bottom-level CNAE (those with a
    code of 5 characters).
    """

    _name = _inherit = "res.partner"

    _columns = {
        "cnae_id": fields.many2one(
            "l10n_es_partner_cnae.cnae_codes",
            domain="[('code', '=ilike', '_____')]",
            string="CNAE Code"),
    }
