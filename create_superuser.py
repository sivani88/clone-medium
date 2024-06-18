import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authors-sivani.settings')
django.setup()

User = get_user_model()

username = 'sivani'
email = 'sivaniavella@gmail.com'
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin_password')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created')
else:
    print('Superuser already exists')
