def server_info_alert(server_info_problematic_ip, server_info_problematic_dict):
    """
    接收系统各项指标测试中不达标的服务器IP和服务器信息, 生成报警邮件内容
    :param server_info_problematic_ip:
    :param server_info_problematic_dict:
    :return:
    """
    print(server_info_problematic_ip)
    print(server_info_problematic_dict)