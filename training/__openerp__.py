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

{
    "name": "Training",
    "version": "3.0",
    "category": "Project",
    "author": "Grupo ESOC",
    "license": "AGPL-3",
    "website": "http://www.grupoesoc.es",
    "installable": True,
    "application": False,
    "summary": "Extend events with training capabilities",
    "depends": [
        "event",
    ],
    "data": [
        "data/training.duration_type.csv",
        "data/training.action_type.csv",
        "security/training.xml",
        "security/ir.model.access.csv",
        "views/menus.xml",
        "views/event.xml",
        "views/action_type.xml",
        "views/action.xml",
        "views/duration_type.xml",
    ],
    "demo": [
        "demo/training.action.csv",
        "demo/training.duration.csv",
        "demo/event.event.csv",
    ],
}
