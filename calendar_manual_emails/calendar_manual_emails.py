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

from openerp import api, fields, models


class EventManualEmails(models.Model):
    """Remove automatic emails for events."""

    _inherit = "calendar.event"

    send_emails_automatically = fields.Boolean(
        string="Send e-mails automatically",
        help="Automatically send mails of changes produced from now on.")

    @api.multi
    def create_attendees(self):
        """Disable mailing in upstream function if needed."""

        return (super(
                    EventManualEmails,
                    self.with_context(
                        no_email=not self.send_emails_automatically))
                .create_attendees())
