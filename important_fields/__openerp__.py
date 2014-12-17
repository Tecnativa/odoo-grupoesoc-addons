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

{
    "name": "Important Fields",
    "version": "2.0",
    "category": "Hidden",
    "summary": "Add a CSS class to highlight important fields in forms",
    "description":
        "This module adds the new CSS class ``.oe_form_important`` "
        "to highlight important fields that are not required.",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "depends": [
        "web",
    ],
    "data": [
        "views/assets.xml",
    ],
}
