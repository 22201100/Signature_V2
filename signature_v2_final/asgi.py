import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signature_v2_final.settings')
application = get_asgi_application()
