from django.contrib import admin
from django.urls import path
from MainMonitor import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server-info-threshold-api', views.ServerInfoThresholdList.as_view()),
    url(r'^server-info-threshold-update/(?P<pk>[0-9]+)/$', views.ServerInfoThresholdUpdate.as_view()),
    path('dashboard/<server_ip>', views.dashboard),
    path('homepage', views.homepage),
    path('iperf-test-alert', views.GetIPerfTestAlertMessage.as_view()),
    path('html-performance-test-alert', views.GetHTMLPerformanceTestAlertMessage.as_view()),
    path('server-info-alert', views.GetServerInfoAlertMessage.as_view()),
]
