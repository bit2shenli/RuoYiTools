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
from common import post_request, get_new_tasks, post_headers, print_curtime

if __name__ == "__main__":
    # TODO 填充 token
    token = "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImY0ZDEyMzhjLTk5ZWYtNDA2Ni1iMGMwLWI0ZDhhMTIzYmZkNSJ9.op-xscDuCqVbjLl58Cw8KnyDdRELI6MvO7izIriRJ79fTzJrl_9eFTm5Fh_jK1QyhU-C2ccuKlhxx6dNe0VbWQ"
    post_headers(token)  # headers 加入 token

    tasks_count = 10        # 每次领取 10 道题
    post_data = {
        "videoTaskQuantity": tasks_count
    }

    while True:

        try:
            results = post_request(get_new_tasks, **post_data)

            if results["code"] == 500 or results["code"] == "500":
                print_curtime(f"{results['msg']}")

            if results["msg"] == "存在未完成的任务，不能获取视频任务":
                print_curtime("已有题目了，冲冲冲")
                break

            if results["stateCode"] == "200":  # 成功获取
                print_curtime(f"已获取 {tasks_count} 道题")
                break

        except KeyError:        # results["code"] = 500     results["msg"] = "当前视频池没有数据"
            print_curtime(f"休息一会，重新尝试获取 {tasks_count} 道题")

        except json.decoder.JSONDecodeError:
            print_curtime(results["msg"])

        except Exception:
            print_curtime("ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。")

        time.sleep(1)

