import os.path
from settings import PROJECT_PATH, DATABASES

def get_status(request):
    is_installed = False
    if os.path.isfile(os.path.join(PROJECT_PATH, DATABASES["default"]["NAME"])):
        is_installed = True
   
    if DATABASES["default"]["ENGINE"] != 'django.db.backends.sqlite3':
        """ using your own engine """
        is_installed = True
         

    print "running status %s"% is_installed
    
    return {
        'is_installed': is_installed,
    }


