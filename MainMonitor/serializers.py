from rest_framework import serializers
from .models import ServerInfoThreshold


class ServerInfoThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfoThreshold
        fields = (
            'cpu_threshold', 'memory_threshold', 'disk_threshold', 'bandwidth_threshold', 'HTML_open_time_threshold',
            'file_transfer_speed_threshold', 'microservices_exec_time_threshold',
            'backend_management_system_open_time_threshold')
