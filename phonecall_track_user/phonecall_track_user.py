# -*- encoding: utf-8 -*-

# OpenERP, Open Source Management Solution
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


class Phonecall(orm.Model):
    _name = _inherit = "crm.phonecall"

    _columns = {
        "user_id": fields.many2one(
            "res.users",
            "Responsible",
            track_visibility="onchange"),
    }

    def write(self, cr, uid, ids, values, context=None):
        """Remove the key `default_state` from the context.

        This key creates a conflict with the mail message that should be sent
        to track the `user_id`, and anyway it is not needed here by
        `crm.phonecall`.
        """

        if context and "default_state" in context:
            context = dict(context)
            del context["default_state"]

        return super(Phonecall, self).write(cr, uid, ids, values,
                                            context=context)
