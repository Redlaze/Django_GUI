from objectpack.ui import BaseEditWindow, make_combo_box, BaseListWindow
from m3_ext.ui import all_components as ext

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission, Group


class PermissionUI(BaseListWindow):
    model = Permission


class UserUI(BaseListWindow):
    model = User


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y')

        self.field__superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='superuser_status',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')


        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            anchor='100%')


        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            anchor='100%')


        self.field__emai_adress = ext.ExtStringField(
            label=u'emai adress',
            name='emai_adress',
            anchor='100%')


        self.field__staff_status = ext.ExtCheckBox(
            label=u'staff status',
            name='staff_status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            anchor='100%')


        self.field__data_joined = ext.ExtDateField(
            label=u'data joined',
            name='data_joined',
            anchor='100%',
            format='d.m.Y')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser,
            self.field__username,
            self.field__emai_adress,
            self.field__first_name,
            self.field__last_name,
            self.field__staff_status,
            self.field__active,
            self.field__data_joined

        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            anchor='100%')

        cont_types = ContentType.objects.all()
        content_list = [(el.id, el.name) for el in cont_types]
        self.field__content_type = make_combo_box(
            label=u'content type',
            name='content_type_id',
            anchor='100%',
            data=content_list,
            display_field='name')

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            anchor='100%',)


    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'