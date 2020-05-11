from django.shortcuts import render
from .models import ServerInfoThreshold
from .serializers import ServerInfoThresholdSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ipware.ip import get_ip


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
        server_ip_dict = dict(request.data)
        ip = get_ip(request)
        print(ip)
        print(server_ip_dict['server_ip'])
        return Response(status.HTTP_200_OK)


class GetHTMLPerformanceTestAlertMessage(APIView):
    """
    从子服务器中获取前端性能检验结果不达标的URL列表
    """
    def post(self, request):
        url_dict = dict(request.data)
        ip = get_ip(request)
        print(ip)
        print(url_dict['url'])
        return Response(status.HTTP_200_OK)
