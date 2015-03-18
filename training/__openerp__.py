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
    "version": "1.0",
    "category": "Project",
    "author": "Grupo ESOC",
    "license": "AGPL-3",
    "website": "http://www.grupoesoc.es",
    "installable": True,
    "application": False,
    "summary": "Extend events with training capabilities",
    "description": """
Training
========

This module helps you organize your trainings.

How does it work?
-----------------

This module installs the *event* module and extends it with training
capabilities.

A **training action** is a definition of a course. Thus, you can have a catalog
of courses that you offer. Training actions define the **amount of hours** of
each type that should be teached.

Each training action can belong to a **training type**, which then defines what
**type of hours** are expected in those training actions.

For instance:

- A training of type *on-site* may expect only *on-site* hours.

- A training of type *online* may expect only *online* hours.

- A training of type *mixed* may expect both *on-site* and *online* hours.

A **training group** is an event that has a training action linked. You can
have as many training groups as you wish for each training action.

A **tutor** is a special teacher that oversees the whole group. Whenever a
student has a doubt in a non-on-site class, they usually reach a tutor (via
email, phone, etc.) to ask them. Also, tutors may actively review the students'
progress. You can have as many tutors as you want for each training group.

All these things can be configured as you wish.
""",
    "depends": [
        "event",
    ],
    "data": [
        "security/training.xml",
        "security/ir.model.access.csv",
        "views/menus.xml",
        "views/event.xml",
        "views/action_type.xml",
        "views/action.xml",
        "views/duration_type.xml",
    ],
}
