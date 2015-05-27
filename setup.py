# -*- encoding: utf-8 -*-
"""
Python setup file for the countries app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

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
