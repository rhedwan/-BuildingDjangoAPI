from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


"""
LINKS: https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
1. This used for auto-generating the token for the user as soon a their detaills get 
to the database.

"""