# -*- coding: utf-8 -*-
from model.group import Group
import pytest
# from data.add_group import constant as testdata
from data.groups import testdata


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_grouptest(app, db, data_groups):
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_groups_list()
    group = data_groups
    # old_groups = app.group.get_groups_list()
    with pytest.allure.step("When I add the group %s to the list" % group):
        app.group.init_new_group_creation()
        app.group.fill_group_form(group)
        app.group.submit_new_group_creation()
    # assert len(old_groups) + 1 == app.group.count()
    # new_groups = app.group.get_groups_list()
    with pytest.allure.step("Then the new group list is equal to the old group list with added group"):
        new_groups = db.get_groups_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
