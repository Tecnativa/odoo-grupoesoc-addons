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

class PartnerVATInContacts(orm.Model):
    """Allow to set up individual VAT for a company"s contacts."""

    _name = _inherit = "res.partner"

    _columns = {
        "contact_vat": fields.char(
            "Contact TIN",
            size=32,
            help="Tax Identification Number of the contact. "
                 "This will not be used for commercial actions; "
                 "instead, parent company's TIN will be used."),
    }
