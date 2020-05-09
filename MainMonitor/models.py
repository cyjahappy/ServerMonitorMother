from django.db import models


# 存储系统各项阈值的数据
class ServerInfoThreshold(models.Model):
    id = models.FloatField(primary_key=True)
    cpu_threshold = models.FloatField(default=90.0)
    memory_threshold = models.FloatField(default=90.0)
    disk_threshold = models.FloatField(default=90.0)
    bandwidth_threshold = models.FloatField(default=3.0)
    HTML_open_time_threshold = models.FloatField(default=3.0)
    file_transfer_speed_threshold = models.FloatField(default=0.0)
    microservices_exec_time_threshold = models.FloatField(default=0.0)
    backend_management_system_open_time_threshold = models.FloatField(default=0.0)
