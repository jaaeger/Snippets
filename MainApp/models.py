from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.http import request


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=False, null=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/snippets/list/{self.id}'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
