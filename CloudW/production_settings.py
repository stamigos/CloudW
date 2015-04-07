# production settings

ALLOWED_HOSTS = ['clw.com.ua']
#DEBUG = False
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
