from setuptools import setup, find_packages

setup(
    name='gui_djano',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47'
    ],
)