from django.db import models
from django.contrib.auth.models import User #Built in Django User model
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk' : self.pk})