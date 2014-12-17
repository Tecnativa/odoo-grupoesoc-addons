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
    'name': 'Partner Origin',
    'version': '3.0',
    'category': 'Customer Relationship Management',
    'summary': 'Tool to know the partner that presented you another partner',
    'description':
"""
This module adds the "origin" field in the partner object.

There you can select other partner that presented you that one.
""",
    'author': 'Grupo ESOC',
    'website': 'http://www.grupoesoc.es',
    'license': 'AGPL-3',
    "installable": True,
    "depends" : ['crm'],
    "data" : [
        'view/partner.xml',
    ],
}
