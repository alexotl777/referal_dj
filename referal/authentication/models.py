from django.db import models

# Create your models here.

class authentication(models.Model):
    phone = models.CharField(max_length=255)
    invite = models.CharField(max_length=255)
    def __str__(self):
        return self.phone