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

from openerp import api, fields, models


class PartnerVATInContacts(models.Model):
    """Allow to set up individual VAT for a company"s contacts."""

    _inherit = "res.partner"

    contact_vat = fields.Char(
        "Contact TIN",
        size=32,
        help="Tax Identification Number of the contact. "
             "This will not be used for commercial actions; "
             "instead, parent company's TIN will be used.")

    @api.one
    def best_vat_field(self):
        """Get the best VAT field name available."""

        return "vat" if self.is_company else "contact_vat"

    @api.one
    def best_vat_value(self):
        """Automatically choose the best VAT value available."""

        return getattr(self, self.best_vat_field()[0])
