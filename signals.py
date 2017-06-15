from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from workey_app.models import Worker

@receiver(post_save, sender=User, dispatch_uid='a1b2c4d4')
def create_worker(sender, instance, **kwargs):
     created = kwargs.get('created')
     if created:
         Worker.objects.create(user=instance)


@receiver(post_save, sender=User,dispatch_uid='a1b2c4d4')
def update_worker(sender, instance, **kwargs):
     created = kwargs.get('created')
     if not created:
         Worker.objects.save()




