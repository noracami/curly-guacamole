from django.conf import settings
from django.db import models

# Create your models here.
#class Store(models.Model):
    #

class Shift(models.Model):
    # 日期, 輪值人員, 代班人員, 確認
    date = models.DateField('日期', auto_now_add=True)
    is_holiday = models.BooleanField('例假日')
    worker = models.ForeignKey('workers.Worker', related_name='shifts_worker')
    substitute = models.ForeignKey('workers.Worker', related_name='shifts_substitute')
    confirm = models.ForeignKey('workers.Worker', related_name='shifts_confirm')

    class Meta:
        verbose_name = '班'

    def __str__(self):
        return self.date

class Table(models.Model):
    # month, shifts, worker, supervisor
    date = models.DateField('日期')
    worker = models.ForeignKey('workers.Worker', related_name='table_worker')
    supervisor = models.ForeignKey('workers.Worker', related_name='table_supervisor')

    class Meta:
        verbose_name = '每月輪值表'

    def __str__(self):
        return '%s年%s月輪值表' % (self.date.year, self.date.month)
