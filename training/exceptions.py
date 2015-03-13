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


class TrainingActionValidationError(exceptions.ValidationError):
    def __init__(self, value):
        super(TrainingActionValidationError, self).__init__(value)
        self.name = _("Error(s) with the training action.")


class WrongDurationType(TrainingActionValidationError):
    def __init__(self,
                 invalid_hour_type,
                 valid_hour_types,
                 value=_("Hour type '%s' is not among the valid ones "
                         "defined in the training type (%s).")):
        self.invalid_hour_type = invalid_hour_type
        self.valid_hour_types = valid_hour_types
        value = value % (invalid_hour_type.name,
                         ", ".join(valid_hour_types.mapped("name")))
        super(WrongDurationType, self).__init__(value)
