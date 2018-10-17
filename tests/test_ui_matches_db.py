from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    # ui_list =
    print(timeit(lambda: app.group.get_groups_list(), number=1))

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    #db_list =
    print(timeit(lambda: map(clean, db.get_groups_list()), number=3000))
    # assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
