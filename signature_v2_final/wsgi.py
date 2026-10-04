import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signature_v2_final.settings')
application = get_wsgi_application()
