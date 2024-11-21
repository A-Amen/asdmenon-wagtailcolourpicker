Wagtail Colour Picker
=====================

A colour picker for Wagtail's DraftJS editor. 
[Original repo](https://github.com/AccentDesign/wagtailcolourpicker/)
[Forked repo](https://github.com/developersociety/civicus-wagtailcolourpicker)


Installation
---
`
pip install wagtailrichtextcolourpicker
`
   
Setup
---

Add `colorfield` and `wagtailcolourpicker` to INSTALLED_APPS in your settings. Ensure this is added after you have added all other django/wagtail modules.
  
```python
   INSTALLED_APPS = [
      ...
       'colorfield'
       'wagtailcolourpicker',
      ...
   ]
```
Settings  
---
  

   #### Picker icon setting
   ` WAGTAILCOLOURPICKER_ICON = ['...'] `

   Use an icon name from the [wagtail registered icon list](https://docs.wagtail.org/en/stable/advanced_topics/icons.html) or register [your own icon with hooks](https://docs.wagtail.org/en/v5.2.7/advanced_topics/icons.html#add-a-custom-icon)

Models
------

To add a color, go to Snippets -> Color

![image info](snippet.png)

All added colors are then registered to the richtext features. 

Screenshots
-----------

.. figure::  http://wagtailcolourpicker.readthedocs.io/en/latest/_images/screen_1.png
   :width: 728 px

Picker

![image info](example.png)

Selected Text

![image info](selected.png)

Example app
------------------------

* Clone the repo

   ```bash
   git clone https://github.com/A-Amen/asdmenon-wagtailcolourpicker.git
   ```

* Install dependencies
   ```python
   pip install -r requirements.txt'
   ```
* Migrate 

   ```python
   python manage.py migrate
   ```
* Create a superuser
  ```python
   python manage.py createsuperuser
   ```
* Then runserver.
   ```python
   python manage.py runserver
   ```


Go to http://127.0.0.1:8000/admin and add a new Basic page to test your changes.

Example site with docker
------------------------

Clone the repo


```bash
git clone https://github.com/A-Amen/asdmenon-wagtailcolourpicker.git
```

Run the docker container

```bash
   cd wagtailcolourpicker
   docker-compose up
```

Create yourself a superuser

```bash
    docker-compose exec app bash
    python manage.py createsuperuser
```

Go to http://127.0.0.1:8000/admin and add a new basic page