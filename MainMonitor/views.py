from django.shortcuts import render
from .models import ServerInfoThreshold
from .serializers import ServerInfoThresholdSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ipware.ip import get_ip
from .iperf_alert import iperf_alert
from .html_performance_alert import html_performance_alert
from .server_info_alert import server_info_alert


class ServerInfoThresholdList(generics.ListAPIView):
    """
    定义GET操作,返回JSON格式的服务器各项指标阈值(REST)   待更新!!!
    """
    queryset = ServerInfoThreshold.objects.all()
    serializer_class = ServerInfoThresholdSerializer


class ServerInfoThresholdUpdate(generics.UpdateAPIView):
    """
    定义PUT操作,更新服务期各项指标阈值(REST)           待更新!!!
    """
    queryset = ServerInfoThreshold.objects.all()
    serializer_class = ServerInfoThresholdSerializer


def dashboard(request):
    """
    渲染Dashboard前端页面     目前用来测试调整阈值的API,待更新!!!
    """
    return render(request, 'Dashboard.html', locals())


class GetIPerfTestAlertMessage(APIView):
    """
    从子服务器中获取iPerf3检验结果不达标的IP地址列表
    """

    def post(self, request):
        iperf3_problematic_target_server_dict = dict(request.data)
        iperf3_problematic_source_ip = get_ip(request)
        iperf_alert(iperf3_problematic_source_ip, iperf3_problematic_target_server_dict)
        return Response(status.HTTP_200_OK)


class GetHTMLPerformanceTestAlertMessage(APIView):
    """
    从子服务器中获取前端性能检验结果不达标的URL列表
    """

    def post(self, request):
        html_performance_problematic_target_url_dict = dict(request.data)
        html_performance_problematic_source_ip = get_ip(request)
        html_performance_alert(html_performance_problematic_source_ip, html_performance_problematic_target_url_dict)
        return Response(status.HTTP_200_OK)


class GetServerInfoAlertMessage(APIView):
    """
    从子服务器中接收系统各项指标超过阈值的报警信息
    """

    def post(self, request):
        server_info_problematic_dict = dict(request.data)
        server_info_problematic_ip = get_ip(request)
        server_info_alert(server_info_problematic_ip, server_info_problematic_dict)
        return Response(status.HTTP_200_OK)
