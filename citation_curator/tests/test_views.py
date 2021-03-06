# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from nose.plugins.attrib import attr
from .mixins import DiamondTestCase


class ViewTestCase(DiamondTestCase):
    def test_login(self):
        "ensure the login screen loads"
        rv = self.client.get('/user/login')
        assert b"Login" in rv.data

    def test_index(self):
        "ensure index is redirecting"
        rv = self.client.get('/')
        assert rv.status_code == 302
