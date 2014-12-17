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
    "name": "Show Always Partner Type Icon",
    "version": "2.0",
    "category": "Tools",
    "summary": "Add the default gray building/person icon to partners form",
    "description":
        "To make it easier to know if a partner is a company or a contact, "
        "this module adds the default logo of a building or a person to every "
        "partner in the form.",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends" : [
        "base",
    ],
    "data" : [
        "view/res_partner.xml",
    ],
}
