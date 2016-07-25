# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from ..models import Role, User


def typical_workflow():
    "create some example objects"

    Role.add_default_roles()
    User.add_guest_user()
