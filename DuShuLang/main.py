# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : login_system
  Description : 登录 + 查询任务状态 + 统计任务状态
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/5/6 23:59
-------------------------------------------------
"""
from common import post_request, login_interface, post_headers, get_user_task, get_request, post_pending_task, \
    post_receive_task, print_curtime


def login():
    """ 登录获取 token """
    post_data = {
        "username": "",
        "password": "",
        "captcha": "054677",  # TODO
        "captchaId": "XQo1qYRMAUn7HaUmqYRF"  # TODO
    }

    login_data = post_request(login_interface, **post_data)
    if login_data["code"] != 0:
        print_curtime(f"错误代码：{login_data['code']}")
        print_curtime(f"错误内容：{login_data['msg']}")

        return False

    # 成功时载入 token 到 header
    data = login_data["data"]
    token = data["token"]
    print_curtime(f"token:\n{token}\n")
    post_headers(token)  # headers 加入 token
    # print_curtime(get_headers())

    return True


if __name__ == "__main__":
    login()