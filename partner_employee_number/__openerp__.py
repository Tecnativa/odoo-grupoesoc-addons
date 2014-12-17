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

{
    "name": "Partner Employee Number",
    "version": "1.0",
    "category": "Customer Relationship Management",
    "summary": "Number of employees that a partner has",
    "description":
"""
This module adds one field to the partner object: number of employees.

This field is unrelated to any other modules, and is intended to be filled
by hand.
""",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends" : ["base"],
    "data" : [
        "view/partner.xml",
    ],
}
