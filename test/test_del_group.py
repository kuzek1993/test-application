from model.group import Group
import random

def test_del_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group(Group(name="new group"))
    old_list = app.groups.get_group_list()
    index = random.randrange(0, len(old_list))
    app.groups.delete_group(index)
    new_list = app.groups.get_group_list()
    group = old_list[index]
    old_list.remove(group)
    assert sorted(new_list) == sorted(old_list)