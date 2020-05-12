def html_performance_alert(html_performance_problematic_source_ip, html_performance_problematic_target_url_dict):
    """
    接收前端性能测试中不达标的URL信息, 生成报警邮件的内容
    :param iperf3_problematic_source_ip:
    :param iperf3_problematic_target_server_dict:
    :return:
    """
    html_performance_problematic_target_server_ip = list(html_performance_problematic_target_url_dict.keys())
    html_performance_problematic_test_results = list(html_performance_problematic_target_url_dict.values())
    print(html_performance_problematic_target_server_ip)
    print(html_performance_problematic_test_results)