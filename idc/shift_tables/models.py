from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#class Store(models.Model):
    #

class Shift(models.Model):
    # 日期, 輪值人員, 代班人員, 確認
    date = models.DateField('日期', default=timezone.now)
    is_holiday = models.BooleanField('例假日')
    worker = models.ForeignKey('workers.Worker', related_name='shifts_worker', blank=True, null=True)
    substitute = models.ForeignKey('workers.Worker', related_name='shifts_substitute', blank=True, null=True)
    confirm = models.ForeignKey('workers.Worker', related_name='shifts_confirm', blank=True, null=True)

    class Meta:
        verbose_name = '班'

    def __str__(self):
        return '%s' % self.date

class Table(models.Model):
    # month, shifts, worker, supervisor
    date = models.DateField('日期')
    worker = models.ForeignKey('workers.Worker', related_name='table_worker', blank=True, null=True)
    supervisor = models.ForeignKey('workers.Worker', related_name='table_supervisor', blank=True, null=True)

    class Meta:
        verbose_name = '每月輪值表'

    def __str__(self):
        return '%s年%s月輪值表' % (self.date.year, self.date.month)
