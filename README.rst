.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================
Business ID and VAT fields
==========================
* Adds a new Business ID field
* Shows the Business ID and core's VAT field only for appropriate companies, based on their country groups
* Restricts Business IDs so that they must be unique

Installation
============
* Just install the module

Configuration
=============
* Set system parameter sale_business_id.show_for_child_companies to True or False based on whether you want to show the Business ID and VAT fields for companies that have a parent company defined.
* Configure the Country Groups at Sales -> Configuration -> Contacts -> Localization -> Country Group. By default Business ID is shown for Finnish companies, and VAT for European countries

Usage
=====
* Set the Business ID and VAT in the partner form

Known issues / Roadmap
======================
* None

Credits
=======

Contributors
------------
* Timo Talvitie <timo@vizucom.com>

Maintainer
----------
.. image:: http://vizucom.com/logo.png
   :alt: Vizucom Oy
   :target: http://www.vizucom.com


This module is maintained by Vizucom Oy
