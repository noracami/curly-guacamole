from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField('姓名', max_length=40)
    password = models.CharField('密碼', max_length=40, blank=True)
    email = models.EmailField('Email', blank=True)
    account = models.CharField('帳號', max_length=40,blank=True)

    class Meta:
        verbose_name = '人員'

    def __str__(self):
        return self.name
