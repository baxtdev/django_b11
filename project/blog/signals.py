from django.db.models.signals import post_save,pre_save,post_migrate
from django.dispatch import receiver
from accounts.models import CustomUser as User

from .models import News

from .utils import send_message_to_email

@receiver(post_save, sender=News)
def send_notify_in_create_news(sender, instance:News, created, **kwargs):
    print(f"News-{instance.id}-создался")
    if created:
        users = User.objects.all()
        user_email = [user.email for user in users]
        result = send_message_to_email(
            'New object in our portal',f'Переходи по ссылке - http://127.0.0.1:8000/{instance.id}',user_email
        )