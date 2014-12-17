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
    'name': 'Partner Projects',
    "version": "2.0",
    'category': 'Project Management',
    'summary': 'Quickly view all projects from a partner',
    'description':
        "Add a button to the partners view to see its related projects.",
    'author': 'Grupo ESOC',
    'website': 'http://www.grupoesoc.es',
    'license': 'AGPL-3',
    "installable": True,
    "depends" : [
        "analytic",
        "project",
    ],
    "data" : [
        'view/partner.xml',
    ],
}
