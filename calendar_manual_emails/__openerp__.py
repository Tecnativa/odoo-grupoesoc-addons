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
    "name": "Manual e-Mails For Calendar Events",
    "version": "1.0",
    "category": "Personal & Shared Calendar",
    "summary": "Disable automatic e-mails for event attendees",
    "description": """
Odoo invites all attendees to any event by e-mail by default.

If you don't want your customers to recieve those invitations, and prefer to
keep your agenda private, this module is for you.

This module disables automatic e-mails that usually are sent to
event attendees unless you manually check the provided checkbox.

If you enable the checkbox, then any further changes will be sent.

If you prefer to send notifications manually, a button is added for it.
""",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["calendar"],
    "data": [
        "views/calendar_manual_emails.xml",
    ],
}
