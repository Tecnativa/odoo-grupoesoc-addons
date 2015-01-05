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

"""Module to check automatically contact's VAT number.

Many code has been copied from `mod:openerp.addons.base_vat.base_vat`.
"""

import string
from openerp.addons.base_vat.base_vat import _ref_vat
from openerp.osv import fields, orm
from openerp.tools.translate import _


class PartnerVATInContacts(orm.Model):
    """Check contacts' VAT numbers."""

    _name = _inherit = "res.partner"

    def _constraint_msg_contact_vat(self, cr, uid, ids, context=None):

        def default_vat_check(cn, vn):
            # by default, a VAT number is valid if:
            #  it starts with 2 letters
            #  has more than 3 characters
            return (cn[0] in string.ascii_lowercase and
                    cn[1] in string.ascii_lowercase)

        vat_country, vat_number = self._split_vat(
            self.browse(cr, uid, ids)[0].contact_vat)

        vat_no = _("'CC##' (CC=Country Code, ##=VAT Number)")

        if default_vat_check(vat_country, vat_number):
            vat_no = _ref_vat.get(vat_country, vat_no)

        return "\n" + _("This VAT number does not seem to be valid.\n"
                        "Note: the expected format is %s") % vat_no

    def button_check_contact_vat(self, cr, uid, ids, context=None):
        if not self.check_contact_vat(cr, uid, ids, context=context):
            msg = self._constraint_msg_contact_vat(
                cr, uid, ids, context=context)
            raise osv.except_osv(_('Error!'), msg)

        return True

    def check_contact_vat(self, cr, uid, ids, context=None):
        """Check validity of `contact_vat`.

        It does not use VIES because usually it would fail when checking
        persons' VATs.
        """

        for partner in self.browse(cr, uid, ids, context=context):
            if partner.is_company or not partner.contact_vat:
                continue

            vat_country, vat_number = self._split_vat(partner.contact_vat)

            if not self.simple_vat_check(cr, uid, vat_country, vat_number,
                                         context=context):
                return False

        return True

    _constraints = [(check_contact_vat,
                     _constraint_msg_contact_vat,
                     ["contact_vat"])]
