from pytest_bdd import given, when, then
from model.group import Group
import random
import pytest

# Groups Lists:


@pytest.allure.step("Given a group list")
@given("a group list")
def group_list(db):
    old_groups = db.get_groups_list()
    return old_groups


@pytest.allure.step("Given a non-empty group list")
@given("a non-empty group list")
def non_empty_group_list(db, app):
    if len(db.get_groups_list()) == 0:
        app.group.init_new_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_new_group_creation()
    old_groups = db.get_groups_list()
    return old_groups


# Groups:


@pytest.allure.step("Given a group name={name}, header={header} and footer={footer}")
@given("a group <name>, <header> and <footer>")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@pytest.allure.step("Given a random group from the list")
@given("a random group from the list")
def a_random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when("I add the group to the list")
def add_new_group(app, new_group):
    with pytest.allure.step("When I add the group to the list"):
        app.group.init_new_group_creation()
        app.group.fill_group_form(new_group)
        app.group.submit_new_group_creation()


@when("I delete the random group from the list")
def delete_random_group(app, a_random_group):
    with pytest.allure.step("When I delete the random %s group from the list" % a_random_group):
        app.group.del_group_by_id(a_random_group.id)


@then("the new group list is equal to the old group list with added group")
def verify_group_added(db, group_list, new_group):
    with pytest.allure.step("Then the new group list is equal to the old group list with added group"):
        old_groups = group_list
        new_groups = db.get_groups_list()
        old_groups.append(new_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@then("the new group list is equal to the old group list without the deleted group")
def verify_group_deletion(app, db, non_empty_group_list, a_random_group, check_ui):
    with pytest.allure.step("Then the new group list is equal to the old group list without the deleted group"):
        old_groups = non_empty_group_list
        new_groups = db.get_groups_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(a_random_group)
        assert old_groups == new_groups
        # if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
