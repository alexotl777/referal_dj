from django.db import models

# Create your models here.

class authentication(models.Model):
    phone = models.CharField(max_length=255)
    invite = models.CharField(max_length=255)
    invite_activated = models.BooleanField(verbose_name='Активирован код', default=False)
    def __str__(self):
        return self.phone