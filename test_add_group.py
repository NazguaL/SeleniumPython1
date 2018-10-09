# -*- coding: utf-8 -*-
from application import Application
from group import Group
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy_fixture)
    return fixture


def test_add_grouptest(app):
    app.login(username="admin", password="secret")
    app.init_new_group_creation()
    app.fill_group_form(Group(name="123", header="defaul group header", footer="defaul group footer"))
    app.submit_new_group_creation()
    app.logout()


def test_add_empty_grouptest(app):
    app.login(username="admin", password="secret")
    app.init_new_group_creation()
    app.fill_group_form(Group(name="", header="", footer=""))
    app.submit_new_group_creation()
    app.logout()

