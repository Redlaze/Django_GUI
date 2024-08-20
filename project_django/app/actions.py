from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission, Group

from .ui import UserAddWindow, PermissionAddWindow, UserUI, PermissionUI

class ContentTypeActionPack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = add_to_desktop = True


class UserActionPack(ObjectPack):
    model = User
    list_window = UserUI
    add_window = edit_window = UserAddWindow
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'header': 'password',
            'data_index': 'password'
        },
        {
            'header': 'last login',
            'data_index': 'last_login'
        },
        {
            'header': 'superuser status',
            'data_index': 'is_superuser'
        },
        {
            'header': 'username',
            'data_index': 'username'
        },
        {
            'header': 'first name',
            'data_index': 'first_name'
        },
        {
            'header': 'last name',
            'data_index': 'last_name'
        },
        {
            'header': 'email adress',
            'data_index': 'email'
        },
        {
            'header': 'staff status',
            'data_index': 'is_staff'
        },
        {
            'header': 'active',
            'data_index': 'is_active'
        },
        {
            'header': 'date joined',
            'data_index': 'date_joined'
        },
    ]


class PermissionActionPack(ObjectPack):
    model = Permission
    list_window = PermissionUI
    add_window = edit_window = PermissionAddWindow
    add_to_menu = add_to_desktop = True

    columns = [
        {
            'header': 'name',
            'data_index': 'name',
        },
        {
            'header': 'content_type',
            'data_index': 'content_type',
        },
        {
            'header': 'codename',
            'data_index': 'codename',
        }
    ]


class GroupActionPack(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = add_to_desktop = True

    columns = [
        {'header': 'name', 'data_index': 'name', 'sortable': True}
    ]



