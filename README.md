## Django multiple language translate

##content
[1. Add configuration for translate to settings](#1-add-configuration-for-translate-to-settings)
[2. Change model for translate](#2-change-model-for-translate)
[3. Change templates for translate](#3-change-templates-for-translate)
[4. Make translate files](#4-make-translate-files)
[5. Force default language for site](#5-force-default-language-for-site)
[6. References](#6-references)

---

### 1. Add configuration for translate to settings

In settings.py, add the following(In my case I created folder named locale inside BASE_DIR you can choose another location and specify the location in settings.py).

```python

from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'vi-VI'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
   os.path.join(BASE_DIR, 'polls/locale')
)

LANGUAGES = (
    ('vi', _('Vietnamese')),
    ('en', _('English')),
)

MULTILINGUAL_LANGUAGES = (
    "en-us",
    "vi",
)
```

Add to midlleware:

```python
MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
]
```

### 2. Change model for translate

Add:
```python
from django.utils.translation import gettext_lazy as _
```

Change any text that you want to translate as below sample:

```python
verbose_name = "Question"
```

change to:

```python
verbose_name = _("Question")
```

[Click here for sample file](https://github.com/xuananh1991/django_translation_sample/blob/master/polls/models.py)

### 3. Change templates for translate

Add:
```django template
{% load i18n %}
```

Change any text that you want to translate as below sample:

```django template
Welcom to django admin dashboard
```
change to:

```django template
{% trans "Welcom to django admin dashboard" %}
```

[Click here for sample file](https://github.com/xuananh1991/django_translation_sample/blob/master/templates/admin/base_site.html)

### 4. Make translate files

Create all `locale` directories same as you delared at `LOCALE_PATHS` above

Run the `makemessages` command from any one of the 2 places based on the requirement as the command looks for the translation texts through all the child directories from which it is run.

    a. Project's root directory where manage.py resides.

    b. App's root directory where models.py, views.py resides.

Run command: 

```shell
django-admin.py makemessages -l de
django-admin.py makemessages -l en
django-admin.py makemessages -l fr
django-admin.py makemessages -l es
django-admin.py makemessages -l pt
```

[Click here to check the language codes](https://github.com/xuananh1991/django_translation_sample/blob/master/Python%20Tuple%20Lists%20with%20language%20codes%20(as%20of%20ISO%20639-1)%20and%20country%20codes%20(as%20of%20ISO%203166).md)

or run command for make all language:

```shell
django-admin.py makemessages --all
```

The above command will create a directory named ar inside locale directory with the following folder structure.

```
locale
└── vi
    └── LC_MESSAGES
        └── django.po
```

A small piece in `django.po`

```shell
#: templates/admin/base_site.1.html:12 templates/admin/base_site.html:16
msgid "Welcom to django admin dashboard"
msgstr "Chao mung den voi bang dieu khien django admin"
```

- `msgid` contain the origin text 
- `msgstr` you must fill your translated text here


Now run the compilemessages from the same directory as mentioned above, it will generate `django.mo` file.

```shell
django-admin.py compilemessages
```

The directory structure of loacle directory will look like this.

```
locale
└── vi
    └── LC_MESSAGES
        ├── django.mo
        └── django.po
```

Start server:

```shell
python manage.py runserver
```

Visit http://127.0.0.1:8000/en/admin/ to view/access the English based Admin site
Visit http://127.0.0.1:8000/vi/admin/ to view/access the Vietnam based Admin site


### 5. Force default language for site

Create **`middleware.py`** in project directory as [link](https://github.com/xuananh1991/django_translation_sample/blob/master/django_translation_sample/middleware.py)

Modify in `settings.py`:

- Add midlleware: 

```python
MIDDLEWARE = [
    'django_translation_sample.middleware.force_default_language_middleware',
    'django.middleware.locale.LocaleMiddleware',
```

- change language code to language that you want to set as default
 
```python
LANGUAGE_CODE = 'vi'
```



**Note:** *`django_translation_sample.middleware.force_default_language_middleware`* must be declared before *`django.middleware.locale.LocaleMiddleware`*

Start server:

```shell
python manage.py runserver
```
Visit http://127.0.0.1:8000/admin/ you will be redirected to Vietname page: http://127.0.0.1:8000/vi/admin/

Use can access English version by visit http://127.0.0.1:8000/en/admin/

### 6. References
https://docs.djangoproject.com/en/2.0/topics/i18n/translation/
https://djangobook.com/localization-create-language-files/
https://djangobook.com/internationalization-python-code/
https://djangobook.com/internationalization-template-code/
https://djangobook.com/internationalization-javascript-code/