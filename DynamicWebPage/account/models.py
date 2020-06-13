import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    accountname = models.OneToOneField(User, on_delete=models.CASCADE)

    fullName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profilePhoto = models.URLField(blank=True)

    def __str__(self):
        return "%s" % (self.fullName)

    class Meta:
        db_table = "account"