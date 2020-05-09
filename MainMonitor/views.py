from django.shortcuts import render
from django.http import HttpResponse
from .models import ServerInfoThreshold
from .serializers import ServerInfoThresholdSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ServerInfoThresholdList(generics.ListAPIView):
    """
    定义GET操作,返回JSON格式的服务器各项指标阈值(REST)
    """
    queryset = ServerInfoThreshold.objects.all()
    serializer_class = ServerInfoThresholdSerializer


class ServerInfoThresholdUpdate(generics.UpdateAPIView):
    """
    定义PUT操作,更新服务期各项指标阈值(REST)
    """
    queryset = ServerInfoThreshold.objects.all()
    serializer_class = ServerInfoThresholdSerializer


def dashboard(request):
    """
    渲染Dashboard前端页面
    """
    return render(request, 'Dashboard.html', locals())