
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Visitors(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    visitee = models.CharField(max_length=200)
    visitor = models.CharField(max_length=200)
    motif = models.TextField(null=True, blank=True)
    checked_in = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    leaving_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.visitee

    class Meta:
        order_with_respect_to = 'visitor'