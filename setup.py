# -*- encoding: utf-8 -*-
"""
Python setup file for the countries app.

"""
import os
from setuptools import setup, find_packages
import countries as app


dev_requires = [
    'flake8',
]

install_requires = [
    'valuehorizon-forex',
]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="valuehorizon-countries",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, reusable, countries, regions, cities, ISO-3166, valuehorizon',
    author='Quincy Alexander',
    author_email='qalexander@valuehorizon.com',
    url="https://https://github.com/Valuehorizon/valuehorizon-countries",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    },
    test_suite="countries.tests.runtests.runtests"
)
