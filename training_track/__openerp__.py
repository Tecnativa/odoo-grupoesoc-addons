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
    "name": "Training Tracks",
    "version": "1.0",
    "category": "Project",
    "author": "Grupo ESOC",
    "license": "AGPL-3",
    "website": "http://www.grupoesoc.es",
    "installable": True,
    "application": False,
    "auto_install": True,
    "summary": "Organize training tracks",
    "description": """
Training Tracks
===============

This module combines the power of modules ``training`` and
``website_event_track``.

Event tracks can get a training duration type, so it lets the user know if
the training group has fulfilled all the expected hours for it.
""",
    "depends": [
        "training",
        "website_event_track",
    ],
    "data": [
        "views/event_track.xml",
    ],
    "demo": [
        "demo/event.track.csv",
    ],
}
