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
    "name": "CRM Unassigned Leads Notify",
    "version": "2.0",
    "category": "Customer Relationship Management",
    "summary": "Be notified of unassigned leads",
    "description": """
**You must specify the users that have to be notified.**
If a lead or opportunity is unassigned, they will be notified.

You can choose the notified user(s) after installing the module in
*Settings > Technical > Automation > Automated Actions >
Add followers to unassigned lead/opportunity > Actions > Fields to Change >
Add Followers*.

Remember that those users must have permission for seeing the unassigned leads
and opportunities.
""",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends" : ["sale_crm", "base_action_rule"],
    "data" : [
        "data.xml",
    ],
}
