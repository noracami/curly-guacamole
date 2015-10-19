from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField('', max_length=20)

    class Meta:
        verbose_name = '人員'

    def __str__(self):
        return self.name
