"""
WSGI config for hoa_binh_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hoa_binh_project.settings')

application = get_wsgi_application()
