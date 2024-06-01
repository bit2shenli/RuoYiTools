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
import time
from common import post_request, get_new_tasks, post_headers


if __name__ == "__main__":
    token = "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjA1NjlhMWQzLWE1ODgtNDFmYS04ODg3LTJkNmZlNTc0ZDU4NiJ9.sLG4CC9j7GlzfdmXD55luKY6qfC8aQiJ6RvnXMPAQ2hJc-vB-F8UduYanUznHnis6eeoiMQvqw9FQ9OyKOr8xw"           # 填充 token
    post_headers(token)  # headers 加入 token

    tasks_count = 20
    post_data = {
        "videoTaskQuantity": tasks_count
    }       # 每次领取 20 道题

    while True:
        results = post_request(get_new_tasks, **post_data)
        if results["stateCode"] == "200":       # 成功获取
            print(f"已获取 {tasks_count} 道题")
            break

        print(f"休息一会，重新常识获取 {tasks_count} 道题")
        time.sleep(5)

