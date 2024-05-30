from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birth_date = models.DateTimeField()
    email = models.EmailField()
    organization = models.CharField(max_length=50)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)
    scientific_degree = models.CharField(max_length=50)
    # is_superuser = False

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'
