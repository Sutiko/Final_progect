from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to=f"profile/")
    
    def __str__(self):
        return f"{self.user.username}'s Profile."
