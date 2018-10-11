# -*- coding: utf-8 -*-
from model.group import Group


def test_add_grouptest(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="1234", header="defaul group header", footer="defaul group footer")
    app.group.init_new_group_creation()
    app.group.fill_group_form(group)
    app.group.submit_new_group_creation()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_grouptest(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="", header="", footer="")
    app.group.init_new_group_creation()
    app.group.fill_group_form(group)
    app.group.submit_new_group_creation()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

