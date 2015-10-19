from django.db import models

# Create your models here.
class Store(models.Model):
    #

class Shift(models.Model):
    # 日期, 輪值人員, 代班人員, 確認
    date = models.DateField('日期', auto_now_add=True)
    worker = models.ForeignKey(workers.Worker, related_name='shifts')
    substitute = models.ForeignKey(workers.Worker, related_name='shifts')
    check = models.ForeignKey(workers.Worker, related_name='shifts')
