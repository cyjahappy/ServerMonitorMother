# 用于定义使用Celery框架实现的定时任务和分布式任务
# 部署的时候要改端口!!!!!!!
from celery import shared_task
from .send_request import send_get_request_to_all_child_servers


@shared_task
def check_server_info():
    """
    发送指令使所有子服务器获取并检测系统各项指标
    """
    send_get_request_to_all_child_servers('server-info-to-db')


@shared_task
def html_performance_test():
    """
    发送指令使所有子服务器进行前端性能测试
    """
    send_get_request_to_all_child_servers('html-performance-test-results-to-db')


@shared_task
def iperf_test():
    """
    发送指令使所有子服务器相互进行iPerf3测试
    """
    send_get_request_to_all_child_servers('iperf3-test-results-to-db')


@shared_task
def ping_test():
    """
    发送指令使所有子服务器相互进行Ping测试
    """
    send_get_request_to_all_child_servers('ping-results-to-db')


@shared_task
def clean_database():
    """
    发送指令使所有服务器清理数据库中过期数据
    """
    send_get_request_to_all_child_servers('clean-database-api')
