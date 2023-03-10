from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=255, unique=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='users', blank=True, null=True)
    nip = models.CharField(max_length=255, unique=True)
    points = models.DecimalField(decimal_places=0, max_digits=100, default=0)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    username = models.CharField(max_length=255, null=True, blank=True, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Employers'

    def __str__(self):
        return '{} - {}'.format(
            self.pk,
            self.email,
        )

    def reduce_points(self):
        self.points -= 1
        super().save()

    def purchase_points(self, amount):
        self.points += amount
        super().save()