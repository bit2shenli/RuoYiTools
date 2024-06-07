# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : tasks_timer
  Description : 每5秒，请求获取 20 题一次
  Summary     : 1、先获取 token
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/6/1 15:36
-------------------------------------------------
"""
import json
import time
from datetime import datetime
from common import post_request, get_new_tasks, post_headers


if __name__ == "__main__":
    # TODO 填充 token
    token = "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjI3NTRiMjcyLTNjMDYtNDllNi04ZWM4LWE1ZmY2YmQzZDExZiJ9.tojRWiXX2P_-bvOykiHUFo29ZiWFXX3U2g2ckMVjdDgvDc0jU9RsTxWQ6RNgb7CJWwDPlJqQbKSWdz0B0xQRbg"
    post_headers(token)  # headers 加入 token

    tasks_count = 20
    post_data = {
        "videoTaskQuantity": tasks_count
    }       # 每次领取 20 道题

    while True:
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # 获取当前时间戳

        try:
            results = post_request(get_new_tasks, **post_data)

            if results["msg"] == "存在未完成的任务，不能获取视频任务":
                print(f"{formatted_time}\t\t已有题目了，冲冲冲")
                break

            if results["stateCode"] == "200":  # 成功获取
                print(f"{formatted_time}\t\t已获取{tasks_count}道题")
                break

        except KeyError:        # results["code"] = 500     results["msg"] = "当前视频池没有数据"
            print(f"{formatted_time}\t\t休息一会，重新尝试获取{tasks_count}道题")

        except json.decoder.JSONDecodeError:
            print(f"{results['msg']}")

        time.sleep(1)

