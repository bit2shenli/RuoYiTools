# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : common
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/5/7 19:25
-------------------------------------------------
"""
import datetime
import requests
import json


# TODO 部署偌依系统的网址和各个请求接口名称，记得替换
http_url = "https://book-video-admin.eebbk.net"
captcha_image_interface = "/book-video-admin/captchaImage"    # 获取验证码的图片接口
login_interface = "/book-video-admin/login"                   # 登录
task_interface = "/book-video-admin/bookVideo/videoTask/list"       # 获取任务
get_new_tasks = "/book-video-admin/bookVideo/videoTask"


"""
# TODO
http_url = "https://jyy-api-v2.readboy.com"
captcha_image_interface = "/base/captcha"                     # 获取验证码的图片接口
login_interface = "/base/login"                               # 登录
get_user_task = "/video/GetUserTask"
post_pending_task = "/videoMake/GetPendingTask"
post_receive_task = "/videoMake/ReceiveTask"                    # 领取题目的接口
"""




# token = 'your_token_here'
headers = {'Content-Type': 'application/json'}      # 设置请求头，指定 Content-Type 为 application/json

# 任务状态
task_status_dict = {
    3: "已上传",
    5: "审核待指派",
    6: "待审核",
    7: "审核问题待确认",
    8: "审核不通过",
    9: "品检待分配",
    10: "品检待指派",
    11: "待品检",
    12: "品检问题待确认",
    13: "品检不通过",
    14: "待稽核",
    15: "稽核通过",
    16: "稽核不通过",
    17: "免品检",
    18: "免稽核",
    19: "待效果审核",
    20: "废弃待确认",
    21: "废弃通过",
    22: "废弃驳回",
    23: "审核申诉",
    24: "审核申诉不通过",
    25: "品检申诉",
    26: "品检申诉不通过",
    27: "品检分配退回",
    28: "效果审核通过",
    29: "效果审核不通过",
    30: "待效果品检",
    31: "效果品检中",
    32: "效果品检合格",
    33: "效果品检不合格",
    34: "免效果品检",
    35: "效果打回待确定",
    95: "超时回收",
    98: "错题确认中",
    99: "待制作"
}


def get_request(interface_name, params=None):
    """ get 请求公共方法 """
    # print(f"headers: {headers}, params: {params}")

    try:
        response = requests.get(http_url + interface_name, headers=headers, params=params)  # 发送GET请求

        print(f"{interface_name}: {response.status_code}")  # 打印状态码
        return json.loads(response.text)

    except requests.exceptions.ProxyError:
        print("Please close your proxy, and try again later~")


def post_request(interface_name, **data):
    """ post 请求公共方法 """
    print(f"headers: {headers}")

    json_data = json.dumps(data)
    response = requests.post(http_url + interface_name, data=json_data, headers=headers)

    print(f"{interface_name}: {response.status_code}")      # 打印状态码
    return json.loads(response.text)


def post_headers(new_token):
    """ 修改 headers，加入 token """
    global headers
    headers = {
        'Authorization': f'Bearer {new_token}',
        'Content-Type': 'application/json'
    }
    return headers


def get_headers():
    """ 获取 headers """
    return headers


def get_array():
    results = []
    with open('task_ids.txt', 'r') as f:
        for line in f:
            if line != "\n":
                results.append(line.split("\n")[0])

    return results


def print_curtime(custom_message):
    """
    # 打印当前时间和自定义信息
    :param custom_message: 这是你的自定义信息
    :return:
    """
    # 获取当前时间
    now = datetime.datetime.now()

    # 格式化当前时间
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"{formatted_time} - {custom_message}")


if __name__ == "__main__":
    results = get_array()
    print_curtime(results)
    print_curtime("chenyushen test")
