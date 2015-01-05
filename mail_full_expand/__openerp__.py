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
    "name": "Mail Full Expand",
    "version": "3.0",
    "category": "Social Network",
    "summary": "Expand mail in a big window",
    "description":
"""See the message in a big window with its full content.

Odoo automatically tries to remove blockquotes and signatures from received
mails. That is useful because it removes lots of distraction, but sometimes it
removes important information.

Also, messages are narrow to fit in the conversations views, but sometimes you
receive a mail with predefined width and cannot read it.

This module adds a button to all messages to read them in a floating window
with its full contents.
""",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends" : [
        "mail",
        "web",
    ],
    "data": [
        "views/mail_full_expand.xml",
        "views/assets.xml",
    ],
    "qweb": [
        "static/src/xml/mail_full_expand.xml",
    ],
}
