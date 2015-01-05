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


class CNAECodes(models.Model):
    """Store all CNAE codes."""

    _name = "l10n_es_partner_cnae.cnae_codes"
    _parent_store = True

    code = fields.Char("Code", required=True, size=5)
    description = fields.Char("Description", required=True, size=200)
    name = fields.Char("CNAE Code and description",
                       compute="_full_name",
                       store=True)
    parent_id = fields.Many2one(_name, "Parent CNAE")
    parent_left = fields.Integer("Left parent")
    parent_right = fields.Integer("Right parent")
    child_ids = fields.One2many(_name, "parent_id", "Child CNAE")

    _sql_constraints = [
        ("code_unique", "unique(code)", "CNAE codes must be unique"),
    ]

    @api.one
    @api.depends("code", "description")
    def _full_name(self):
        """Get CNAE code and name together."""

        return "%s - %s" % (self.code, self.description)


class PartnerCNAE(models.Model):
    """Add CNAE field to all partners."""

    _inherit = "res.partner"

    cnae_id = fields.Many2one(
        CNAECodes._name,
        "CNAE Code",
        domain=[('code', '=ilike', '_____')], # Only 5-digit codes
        help="CNAE code assigned to this partner.")
