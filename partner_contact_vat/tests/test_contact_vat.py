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

from openerp.tests.common import TransactionCase


class ContactVATCase(TransactionCase):
    """Test behavior of training contact VAT."""

    def setUp(self):
        super(ContactVATCase, self).setUp()

        self.partner = self.env["res.partner"].create({"name": "something"})

    def test_company(self):
        """Setting a VAT to a company."""

        self.partner.is_company = True
        self.partner.vat = "ES00000000T"

        self.assertEqual(self.partner.best_vat_field()[0], "vat")
        self.assertEqual(self.partner.best_vat_value()[0], "ES00000000T")

    def test_person(self):
        """Setting a VAT to a person."""

        self.partner.is_company = False
        self.partner.contact_vat = "ES00000000T"

        self.assertEqual(self.partner.best_vat_field()[0], "contact_vat")
        self.assertEqual(self.partner.best_vat_value()[0], "ES00000000T")
