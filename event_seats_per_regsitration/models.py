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

from openerp import _, api, exceptions, fields, models


class Event(models.Model):
    """Events enhaced with participants per registration limits."""

    _inherit = "event.event"

    seats_per_registration_max = fields.Integer(
        "Maximum of participants per registration",
        default=0,
        help="Registrations with more than this number of participants will "
             "be forbidden. Set 0 to ignore this setting.")

    seats_per_registration_min = fields.Integer(
        "Minimum of participants per registration",
        default=1,
        help="Registrations with less than this number of participants will "
             "be forbidden.")

    @api.one
    @api.constrains("seats_per_registration_max",
                    "seats_per_registration_min",
                    "seats_max")
    def _check_seats_per_registration_limits(self):
        """Ensure you are not setting an invalid maximum."""

        if self.seats_per_registration_min < 1:
            raise exceptions.ValidationError(
                _("You need at least one participant per registration."))

        if self.seats_per_registration_max != 0:
            if (self.seats_per_registration_max <
                    self.seats_per_registration_min):
                raise exceptions.ValidationError(
                    _("The maximum of participants per registration cannot be "
                      "smaller than the minimum."))

        if self.seats_max != 0:
            if self.seats_per_registration_max > self.seats_max:
                raise exceptions.ValidationError(
                    _("The maximum of participants per registration "
                      "cannot be bigger than the maximum of participants "
                      "for this event."))

        try:
            self.registration_ids._check_seats_per_registration_limits()
        except exceptions.ValidationError as error:
            raise exceptions.ValidationError(
                _("There are already registrations that don't fit in the "
                  "new limits of participants per registration. Change them "
                  "before setting the limits."))

class EventRegistration(models.Model):
    """Event registrations must force the limits imposed in the event."""

    _inherit = "event.registration"

    @api.one
    @api.constrains("event_id", "nb_register")
    def _check_seats_per_registration_limits(self):
        """Ensure the number of reserved seats fits in the limits."""

        if self.event_id.seats_per_registration_max != 0:
            if self.nb_register > self.event_id.seats_per_registration_max:
                raise exceptions.ValidationError(
                    _("You cannot register more than %d participants.") %
                        self.event_id.seats_per_registration_max)

        if self.nb_register < self.event_id.seats_per_registration_min:
            raise exceptions.ValidationError(
                _("You cannot register less than %d participants.") %
                    self.event_id.seats_per_registration_min)

    def _default_seats(self):
        """Set the default number of participants per registration."""

        # Normalize cases when there's no record
        event_id = self.event_id.id or self.env.context.get("active_id", False)

        return (self.env["event.event"].browse(event_id)
                .seats_per_registration_min) or 1

    # Default seats to the minimum
    nb_register = fields.Integer(
        default=_default_seats)
