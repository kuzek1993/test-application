from model.group import Group


def test_add_group(app):
    group = Group(name="new group")
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group.name)
    new_list = app.groups.get_group_list()
    old_list.append(group.name)
    assert sorted(new_list) == sorted(old_list)