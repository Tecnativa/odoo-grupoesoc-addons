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

from openerp import _, api, fields, models
from . import exceptions


# Current module domain
_D = "training.%s"


class HourType(models.Model):
    """Types of the expected hours for training actions.

    See docs for :class:`~.TrainingType`.
    """

    _name = _D % "hour_type"

    name = fields.Char(required=True, index=True, translate=True)

    expected_hours_ids = fields.One2many(
        _D % "expected_hours",
        "hour_type_id",
        "Epected hours of this type in training actions")

    # Need to specify relation name to avoid exceeding the limit of 63
    # characters in PostgreSQL names
    training_type_ids = fields.Many2many(
        _D % "training_type",
        relation="training_action_type_hours_rel",
        string="Training types",
        help="Training types that expect this hour type.")

    _sql_constraints = [("unique_name",
                         "UNIQUE(name)",
                         "Name must be unique.")]


class ExpectedHours(models.Model):
    _name = _D % "expected_hours"

    expected_hours = fields.Float(default=0, required=True)

    hour_type_id = fields.Many2one(
        _D % "hour_type",
        "Hour type",
        required=True)

    training_action_id = fields.Many2one(
        _D % "training_action",
        "Training action",
        required=True)

    @api.one
    @api.constrains("hour_type_id", "training_action_id")
    def check_right_hour_types(self):
        """Check that the hour types are the right ones."""

        expected_types = (self.training_action_id.training_type_id
                          .expected_hour_type_ids)

        if expected_types and self.hour_type_id not in expected_types:
            raise exceptions.WrongHourType(self.hour_type_id, expected_types)

    _sql_constraints = [("training_vs_hours_unique",
                         "UNIQUE(hour_type_id, training_action_id)",
                         "Cannot repeat the hour type in a training action.")]


class TrainingType(models.Model):
    """Types of training actions.

    Depending on the training action type, a training action may expect some
    type of hours. For example:

    - If a training action's type is "on-site", it expects on-site hours.
    - If its type is "online", it expects online hours.
    - If its type is "mixed", it expects both on-site and online hours.

    You can configure it as you wish.
    """

    _name = _D % "training_type"

    name = fields.Char(required=True, index=True, translate=True)

    # Need to specify relation name to avoid exceeding the limit of 63
    # characters in PostgreSQL names
    expected_hour_type_ids = fields.Many2many(
        _D % "hour_type",
        relation="training_action_type_hours_rel",
        string="Expected hour types",
        help="These types of hours are expected in this type of training "
             "action. For example, a training of type 'mixed' may expect "
             "hours of types 'on-site' and 'online'.")

    _sql_constraints = [("unique_name",
                         "UNIQUE(name)",
                         "Name must be unique.")]


class TrainingAction(models.Model):
    """Define training actions.

    A training action is one course that your company teaches and has in its
    catalog of courses.

    They define some requirements that the corresponding event is expected to
    fulfill. Events linked to training actions are considered training groups.
    """

    _name = _D % "training_action"

    name = fields.Char(required=True, index=True, translate=True)

    training_type_id = fields.Many2one(
        _D % "training_type",
        "Training type")

    expected_hours_ids = fields.One2many(
        _D % "expected_hours",
        "training_action_id",
        "Expected hours",
        help="Expected duration of each type of hours for these training "
             "groups.")

    @api.onchange("training_type_id")
    def fulfill_expected_hour_types(self):
        """When choosing a type of training action, fulfill the expected hours.

        There will be 0 hours of each type by default.
        """

        # Remove invalid hour expectations
        valid_hour_types = self.training_type_id.expected_hour_type_ids
        for expected_hours in self.expected_hours_ids:
            if expected_hours.hour_type_id not in valid_hour_types:
                self.expected_hours_ids -= expected_hours

        # Add new hour expectations
        current_hour_types = self.mapped("expected_hours_ids.hour_type_id")
        for hour_type in self.training_type_id.expected_hour_type_ids:
            if hour_type not in current_hour_types:
                self.expected_hours_ids |= self.expected_hours_ids.new(
                    {"hour_type_id": hour_type.id})


class Event(models.Model):
    """Expand events with training actions.

    Events with a training type and a training action are considered training
    groups.
    """

    _inherit = "event.event"

    training_action_id = fields.Many2one(
        _D % "training_action",
        "Training action",
        help="Training action of this event, if it is a course.")

    tutor_ids = fields.Many2many(
        "res.partner",
        string="Tutors",
        help="Teachers that are supposed to oversee every track. These will "
             "be available for students to ask them their doubts.")
