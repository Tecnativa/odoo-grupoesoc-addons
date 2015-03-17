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

"""Test permissions per user profile and model."""


from . import test_permissions_bases as b
from openerp import exceptions as e
from openerp.tests.common import at_install


@at_install(True)
class UnprivilegedDurationTypePermissionsCase(b.UnprivilegedPermissionsCase,
                                              b.DurationTypePermissionsCase):
    pass


@at_install(True)
class UnprivilegedDurationPermissionsCase(b.UnprivilegedPermissionsCase,
                                          b.DurationPermissionsCase):
    pass


@at_install(True)
class UnprivilegedActionTypePermissionsCase(b.UnprivilegedPermissionsCase,
                                            b.ActionTypePermissionsCase):
    pass


@at_install(True)
class UnprivilegedActionPermissionsCase(b.UnprivilegedPermissionsCase,
                                        b.ActionPermissionsCase):
    pass


@at_install(True)
class UnprivilegedEventPermissionsCase(b.UnprivilegedPermissionsCase,
                                       b.EventPermissionsCase):
    pass


@at_install(True)
class UserDurationTypePermissionsCase(b.UserPermissionsCase,
                                      b.DurationTypePermissionsCase):
    pass


@at_install(True)
class UserDurationPermissionsCase(b.UserPermissionsCase,
                                  b.DurationPermissionsCase):
    def setUp(self, *args, **kwargs):
        super(UserDurationPermissionsCase, self).setUp(*args, **kwargs)

        # Expected exceptions
        self.ex_insert = None
        self.ex_update = None
        self.ex_delete = None


@at_install(True)
class UserActionTypePermissionsCase(b.UserPermissionsCase,
                                    b.ActionTypePermissionsCase):
    def setUp(self, *args, **kwargs):
        super(UserActionTypePermissionsCase, self).setUp(*args, **kwargs)


@at_install(True)
class UserActionPermissionsCase(b.UserPermissionsCase,
                                b.ActionPermissionsCase):
    def setUp(self, *args, **kwargs):
        super(UserActionPermissionsCase, self).setUp(*args, **kwargs)

        # Expected exceptions
        self.ex_insert = None
        self.ex_update = None
        self.ex_delete = None


@at_install(True)
class UserEventPermissionsCase(b.UserPermissionsCase,
                               b.EventPermissionsCase):
    def setUp(self, *args, **kwargs):
        super(UserEventPermissionsCase, self).setUp(*args, **kwargs)

        # Expected exceptions
        self.ex_insert = None
        self.ex_update = None
        self.ex_delete = None


@at_install(True)
class ManagerDurationTypePermissionsCase(b.ManagerPermissionsCase,
                                         b.DurationTypePermissionsCase):
    pass


@at_install(True)
class ManagerDurationPermissionsCase(b.ManagerPermissionsCase,
                                     b.DurationPermissionsCase):
    pass


@at_install(True)
class ManagerActionTypePermissionsCase(b.ManagerPermissionsCase,
                                       b.ActionTypePermissionsCase):
    pass


@at_install(True)
class ManagerActionPermissionsCase(b.ManagerPermissionsCase,
                                   b.ActionPermissionsCase):
    pass


@at_install(True)
class ManagerEventPermissionsCase(b.ManagerPermissionsCase,
                                  b.EventPermissionsCase):
    pass
