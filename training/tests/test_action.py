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

from .base import _D, BaseCase


class ActionOnChangeTypeFulfillExpectedDurationTypesCase(BaseCase):
    """Test onchange method fulfill_expected_duration_types().

    That method of training actions gets triggered when changing the action
    type, and is supposed to update the duration_ids field.
    """

    create_method = "new"

    def tearDown(self, *args, **kwargs):
        """All tests end checking that the fulfill was right."""

        # Set the action's type
        self.action.type_id = self.action_type

        # This should be run automatically when on UI
        self.action.fulfill_expected_duration_types()

        # Check that it was fulfilled right
        self.assertEqual(set(self.action.mapped("duration_ids.type_id.name")),
                         set(self.duration_types_good.mapped("name")))

        (super(ActionOnChangeTypeFulfillExpectedDurationTypesCase, self)
         .tearDown(*args, **kwargs))

    def test_when_empty(self):
        """When training action has no duration records at all."""

        pass

    def test_when_full_good(self):
        """Create good duration records for the action."""

        for duration_type in self.duration_types_good:
            self.create(
                "duration",
                {"type_id": duration_type.id,
                 "action_id": self.action.id})

    def test_when_half_good(self):
        """Create only one good duration record for the action."""

        self.create(
            "duration",
            {"type_id": self.duration_types_good[0].id,
             "action_id": self.action.id})

    def test_when_full_bad(self):
        """Create bad duration records for the action."""

        for duration_type in self.duration_types_bad:
            self.create(
                "duration",
                {"type_id": duration_type.id,
                 "action_id": self.action.id})

    def test_when_half_bad(self):
        """Create only one bad duration record for the action."""

        self.create(
            "duration",
            {"type_id": self.duration_types_bad[0].id,
             "action_id": self.action.id})

    def test_when_half_good_half_bad(self):
        """Create only one good and one bad duration record for the action."""

        self.create(
            "duration",
            {"type_id": self.duration_types_good[0].id,
             "action_id": self.action.id})
        self.create(
            "duration",
            {"type_id": self.duration_types_bad[0].id,
             "action_id": self.action.id})
