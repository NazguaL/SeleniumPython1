from model.group import Group
import random


def test_del_some_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.init_new_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_new_group_creation()
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.del_group_by_id(group.id)
    new_groups = db.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


