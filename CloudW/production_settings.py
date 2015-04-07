#production settings
import os
from settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webuser_clw',
        'USER': 'webuser_clw',
        'PASSWORD': 'xYx6tnInXloP',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
