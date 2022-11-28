Wagtail Colour Picker
=====================

A colour picker for Wagtail's DraftJS editor.

Installation
------------

.. code:: bash

   pip install git+https://github.com/Vadim-Karpenko/wagtailcolourpicker.git@04dbcf9e5bab32c0dea1c412856653b4e9193028

Setup
-----

Add to installed app:

.. code:: python

   INSTALLED_APPS = [
      ...
      'wagtailcolourpicker',
      ...
   ]

Settings
--------

.. code:: python

   # picker icon
   WAGTAILCOLOURPICKER_ICON = ['...']
   # Add your colours
   WAGTAILCOLOURPICKER_COLOURS = {
      'black': '#000000',
      'white': '#ffffff'
   }

Models
------
Add into your models.py

.. code:: python

    # Add all colors from 'wagtailcolourpicker'
    # list names into your RichTextField(features=[get_list_features_name()]
    body.features += get_list_colour_features_name()

Documentation
-------------

Can be found on `readthedocs <http://wagtailcolourpicker.readthedocs.io/>`_.

Screenshots
-----------

.. figure::  http://wagtailcolourpicker.readthedocs.io/en/latest/_images/screen_1.png
   :width: 728 px

Picker

.. figure:: http://wagtailcolourpicker.readthedocs.io/en/latest/_images/screen_2.png
   :width: 728 px

Selected Text

Example site with docker
------------------------

Clone the repo

.. code:: bash

    $ git clone https://github.com/AccentDesign/wagtailcolourpicker.git

Run the docker container

.. code:: bash

    $ cd wagtailcolourpicker
    $ docker-compose up

Create yourself a superuser

.. code:: bash

    $ docker-compose exec app bash
    $ python manage.py createsuperuser

Go to http://127.0.0.1:8000/cms and add a new basic page
