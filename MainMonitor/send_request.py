import requests
from .models import ChildServerList

server_ip_all = ChildServerList.objects.all()
total_server_ip = server_ip_all.count()


def send_get_request_to_all_child_servers(path):
    """
    向所有子服务器逐个发送http://[子服务器的IP]/path的GET请求
    :return:
    """
    i = 0
    while i < total_server_ip:
        server_ip = server_ip_all[i].server_ip
        # 部署的时候记得改端口!!!!!!!!!!!!!!!!!!!!!!!!!!!
        url = 'http://' + server_ip + ':8001/' + path
        requests.get(url)
        i = i + 1
