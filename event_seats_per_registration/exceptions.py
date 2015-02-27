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

from openerp import _, exceptions


class SeatsPerRegistrationError(exceptions.ValidationError):
    def __init__(self, value):
        super(SeatsPerRegistrationError, self).__init__(value)
        self.name = _("Error in the limits of participants per registration.")


class NeedAtLeastOneParticipant(SeatsPerRegistrationError):
    def __init__(self,
                 value=_("You need at least one participant "
                         "per registration.")):
        super(NeedAtLeastOneParticipant, self).__init__(value)


class MaxSmallerThanMin(SeatsPerRegistrationError):
    def __init__(self,
                 value=_("The maximum of participants per registration cannot "
                         "be smaller than the minimum.")):
        super(MaxSmallerThanMin, self).__init__(value)


class MaxPerRegisterBiggerThanMaxPerEvent(SeatsPerRegistrationError):
    def __init__(self,
                 value=_("The maximum of participants per registration "
                         "cannot be bigger than the maximum of participants "
                         "for this event.")):
        super(MaxPerRegisterBiggerThanMaxPerEvent, self).__init__(value)


class PreviousRegistrationsFail(SeatsPerRegistrationError):
    def __init__(self,
                 previous_exception,
                 value=_("There are already registrations that don't fit in "
                         "the new limits of participants per registration. "
                         "Change them before setting the limits. "
                         "The error was: '%s'")):
        self.previous_exception = previous_exception
        super(PreviousRegistrationsFail, self).__init__(
            value % previous_exception.value)


class TooFewParticipants(SeatsPerRegistrationError):
    def __init__(self,
                 min,
                 value=_("You cannot register less than %d participants.")):
        self.min = min
        super(TooFewParticipants, self).__init__(value % min)


class TooManyParticipants(SeatsPerRegistrationError):
    def __init__(self,
                 max,
                 value=_("You cannot register more than %d participants.")):
        self.max = max
        super(TooManyParticipants, self).__init__(value % max)
