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

from datetime import datetime
from openerp.tests.common import TransactionCase
from .. import exceptions as e


class TestSeatsPerRegistrationLimits(TransactionCase):
    """Test the minimum limits."""

    def setUp(self):
        """Create a dummy event to work with."""

        super(__class__, self).setUp()

        self._event = self.env["event.event"].create(
            {"name": "Test",
             "date_begin": datetime.now(),
             "date_end": datetime.now()})

    def test_less_than_one_participant(self):
        with self.assertRaises(e.NeedAtLeastOneParticipant):
            self._event.seats_per_registration_min = 0

    def test_max_smaller_than_min(self):
        with self.assertRaises(e.MaxSmallerThanMin):
            self._event.seats_per_registration_min = 10
            self._event.seats_per_registration_max = 9

    def test_max_per_register_bigger_than_max_per_event(self):
        with self.assertRaises(e.MaxPerRegisterBiggerThanMaxPerEvent):
            self._event.seats_max = 10
            self._event.seats_per_registration_max = 11

    def test_previous_registrations_fail_min(self):
        with self.assertRaises(e.PreviousRegistrationsFail):
            self._event.registration_ids.create({"nb_register": 10})
            self._event.seats_per_registration_min = 11

    def test_previous_registrations_fail_max(self):
        with self.assertRaises(e.PreviousRegistrationsFail):
            self._event.registration_ids.create({"nb_register": 10})
            self._event.seats_per_registration_max = 9

    def test_too_few_participants(self):
        with self.assertRaises(e.TooFewParticipants):
            self._event.seats_per_registration_min = 10
            self._event.registration_ids.create({"nb_register": 9})

    def test_too_many_participants(self):
        with self.assertRaises(e.TooManyParticipants):
            self._event.seats_per_registration_max = 10
            self._event.registration_ids.create({"nb_register": 11})

    def test_default_seats(self):
        self._event.seats_per_registration_min = 10
        registration = self._event.registration_ids.create()
        self.assertEqual(10, registration.nb_register, "Bad default value")
