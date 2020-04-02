from django.db import models

# Create your models here.


class UserReport(models.Model):
    name = models.CharField(max_length=15, verbose_name='姓名', help_text="姓名")
    tempture = models.DecimalField( max_digits=3, decimal_places=1, verbose_name="温度", help_text="温度")
    address = models.CharField(max_length=60, verbose_name="地址", help_text="地址")
    date = models.DateField(verbose_name="时间", help_text="时间")
    age = models.IntegerField(verbose_name="年龄", help_text="年龄")
