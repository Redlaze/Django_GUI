# GUI интерфейс CRUD:

## Сборка
### Для сборки приложения используется следующая команда:
``python setup.py sdist --formats=gztar --dist-dir  ./``
### После чего в каталоге появится файл ``gui_djano-0.1.tar.gz``

## Тестирование 
### Для тестирования приложения установите виртуальную среду python3.9 (Linux):
````
vertualenv --python==python3.9 ~/test_env
source test_env/bin/activate
````
### Установка пакета
``pip install gui_djano-0.1.tar.gz  --extra-index-url 
http://pypi.bars-open.ru/simple/  --trusted-host pypi.bars-open.ru``
### Запуск приложения
````
python ~/test_env/lib/python3.9/site-packages/project_django/manage.py migrate
python ~/test_env/lib/python3.9/site-packages/project_django/manage.py runserver
````
