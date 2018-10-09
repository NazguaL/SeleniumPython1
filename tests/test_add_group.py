# -*- coding: utf-8 -*-
from model.group import Group


def test_add_grouptest(app):
    app.group.init_new_group_creation()
    app.group.fill_group_form(Group(name="123", header="defaul group header", footer="defaul group footer"))
    app.group.submit_new_group_creation()


def test_add_empty_grouptest(app):
    app.group.init_new_group_creation()
    app.group.fill_group_form(Group(name="", header="", footer=""))
    app.group.submit_new_group_creation()

