from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'chasehayejoc@gmail.com', 'dajngo_user_admin56780')
    except Exception as e:
        print(f"Error creating superuser: {e}")