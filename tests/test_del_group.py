from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.init_new_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_new_group_creation()
    app.group.del_first_group()

