from .base import *

SECRET_KEY = 'ot*j!_j+910kp2kav@zgo$5swx&19tf=*0p*#2j@+^&0vv&1c@'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
