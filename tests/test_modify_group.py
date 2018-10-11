from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.init_new_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_new_group_creation()
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = Group(name="new group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    old_groups = app.group.get_groups_list()
    group = Group(header="new group header")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


