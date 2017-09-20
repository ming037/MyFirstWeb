# -*- coding: utf-8 -*-
#this is production file
from tutorial.settings.base import *
#override base.py settins here
try:
    from tutorial.settings.local import *
except:
    pass

DEBUG = False
ALLOWED_HOSTS = [*] #지정된 사용자만 production으로 접근 할 수 있도록 한다.
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
