===========================
Countries, by Valuehorizon
===========================

.. image:: https://travis-ci.org/Valuehorizon/valuehorizon-countries.svg?branch=master
   :target: https://travis-ci.org/Valuehorizon/valuehorizon-countries
.. image:: https://coveralls.io/repos/Valuehorizon/valuehorizon-countries/badge.svg
   :target: https://coveralls.io/r/Valuehorizon/valuehorizon-countries
.. image:: https://codeclimate.com/github/Valuehorizon/valuehorizon-countries/badges/gpa.svg
   :target: https://codeclimate.com/github/Valuehorizon/valuehorizon-countries

A Django-based Countries data toolkit. 
It also includes documentation, test coverage and the official ISO-3166 seed data
for all current (and former) countries.
This app is a part of the Valuehorizon application ecosystem.

Why a new Countries app?
=========================

This app is not a fork of the excellent django-countries_ app. The aim of
valuehorizon-countries is to provide similar functionality but to actually include a Country model. 
From an architectural point-of-view, we prefer this method for the following reasons:

- Country data are constantly evolving. ISO-3166 aims to keep track of all recognized countries and their current status.
  For example, in 1991, the country known as Yugoslavia split into several states. We want to be able to keep a "Yugoslavia" object,
  but set its status to something "non-current";
- We want to keep the aforementioned country data as up-to-date as possible. Valuehorizon provides an API to do so;
- We want to make ORM queries on that data; and
- We want the data to be part of the database, and not hard-coded in our source-code. This allows us to maintain the country data
  without changing or adding source code.

Again, this app is not meant to replace django-countries_, but simply to provide similar functionality via Django models and not a field.

.. _django-countries: https://github.com/SmileyChris/django-countries

Contributing
============

Please file bugs and send pull requests to the `GitHub repository`_ and `issue
tracker`_.

.. _GitHub repository: https://github.com/Valuehorizon/valuehorizon-countries/
.. _issue tracker: https://github.com/Valuehorizon/valuehorizon-countries/issues

Commercial Support
==================

This project is sponsored by Valuehorizon_. If you require assistance on
your project(s), please contact us: support@valuehorizon.com.

.. _Valuehorizon: http://www.valuehorizon.com
