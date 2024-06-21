# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : get_tasks
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/6/21 10:47
-------------------------------------------------
"""
import time
from common import post_headers, get_request, get_user_task, post_request, post_pending_task, post_receive_task, \
    print_curtime

if __name__ == "__main__":
    # TODO 填充 token
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVVUlEIjoiMmE0MDMzYzItNWZhOS00Y2NjLThkMjQtM2Q5YzhkNjJmMTg1IiwiSUQiOjE0NjI3MCwiTmlja05hbWUiOiJuaWNrbmFtZSIsIkF1dGhvcml0eUlkIjoiMTAwNTQiLCJBdXRob3JpdHlJZHMiOm51bGwsImV4cCI6MTcxOTU0MzM1NCwiaXNzIjoicW1QbHVzIiwibmJmIjoxNzE4OTM3NTU0fQ.KQ49H0KUjA3NjvVdp1DqrinbD-uD3PJ70iqIElRamug"
    post_headers(token)  # headers 加入 token

    while True:
        user_task = get_request(get_user_task, params={})

        if user_task["code"] == 0 and len(user_task["data"]):
            print_curtime("正在前往领取任务...")

            for task in user_task["data"]:
                task_type = task["taskType"]
                print_curtime(f"正在尝试领取{task_type}...")

                post_data_1 = {"taskType": task_type}
                pending_task = post_request(post_pending_task, **post_data_1)

                if pending_task["code"] == 0 and len(pending_task["data"]):
                    print_curtime("发现任务，准备领取...")
                    for p_task in pending_task["data"]:
                        course_id = p_task["courseId"]
                        task_count = p_task["taskCount"]
                        print_curtime(f"课程ID： {course_id} 有课程数量：{task_count}")

                        post_data_2 = {
                            "courseId": course_id,
                            "taskType": task_type
                        }

                        receive_task = post_request(post_receive_task, **post_data_2)
                        if receive_task["code"] != 0:
                            print_curtime("未领取到题目，准备重新尝试 >>>> ", receive_task["msg"])
                        else:
                            print_curtime("领取成功，冲冲冲 >>> ")

        else:
            print_curtime("暂时没有题目，正在准备重新获取...")

        time.sleep(1)