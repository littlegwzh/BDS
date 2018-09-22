from django.db import models


# Create your models here.
class Station(models.Model):
    floor = models.IntegerField('楼层')
    area = models.CharField('区域', max_length=5)
    line = models.CharField('产线', max_length=5)
    station = models.CharField('工位', max_length=8)
    order = models.IntegerField('工位顺序')

    def __str__(self):
        return self.station    # 在django admin中显示

    def __str__(self):
        return self.floor

    class Meta:
        db_table = "bds_station"  # 自定义表名称
        ordering = ['order']     # 按指定字段排序
