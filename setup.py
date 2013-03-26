# -*- coding: utf-8 -*-
""""""

from setuptools import setup, find_packages

setup(
    name='noodle.plugins.pysmbc',
    version='0.1',
    author='',
    author_email='',
    url='https://github.com/noodle-ng/noodle.plugins.pysmbc/',
    license='',
    description='Noodle NG Plugin for CIFS filesystems using pysmbc',
    long_description=open('README.md').read(),
    install_requires=[
        'noodle.core',
    ],
    packages=find_packages(exclude=['tests']),
    namespace_packages=['noodle', 'noodle.plugins'],
    entry_points={'noodle.plugins': 'psymbc = noodle.plugins.pysmbc'},
)
