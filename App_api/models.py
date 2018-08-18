from django.db import models

# Create your models here.

class App_api(models.Model):
    sectionname = models.CharField('模块名称', max_length=64)
    sectiondesc = models.CharField('模块描述', max_length=200)
    sectionmaker = models.CharField('模块负责人', max_length=200)
    create_time = models.DateTimeField('船舰时间', auto_now=True)
    class Meta:
        verbose_name = '模块管理'
        verbose_name_plural = '模块管理'
    def __str__(self):
        return self.sectionname
    