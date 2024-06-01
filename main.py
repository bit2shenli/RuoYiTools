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
import copy

from common import post_request, login_interface, post_headers, task_interface, get_request, get_headers, \
    task_status_dict, get_array


def get_question_status1():
    """ 获取任务信息 """
    page_num, page_size, statistics_total = 1, 20, 0  # statistics_total 本次统计数量
    my_statistics = copy.deepcopy(task_status_dict)  # 深拷贝复制

    while True:
        params = {
            "pageNum": page_num,
            "pageSize": page_size,
            "taskStatusList": [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29,
                               30, 31, 32, 33, 34, 35, 95, 98]
        }  # 98: "错题确认中"
        task_data = get_request(task_interface, params=params)
        # print(task_data)

        # 如果已经找满了数据就开溜（但是中途可能会加入数据，所以尽可能在查询的时候先不要动后台）
        if statistics_total == task_data["total"]:
            break

        # 开始逐一分析数据
        for row in task_data["rows"]:
            statistics_total += 1

            task_id, task_status = row["questionId"], row["taskStatus"]  # 任务ID、任务状态
            task_statistics = my_statistics.get(task_status, "task_status_name:0")

            if len(task_statistics.split(":")) == 2:
                task_status_name, task_status_num = task_statistics.split(":")[0], int(
                    task_statistics.split(":")[1]) + 1
                my_statistics[task_status] = f"{task_status_name}:{task_status_num}"

            else:
                my_statistics[task_status] = f"{my_statistics[task_status]}:1"  # 第一次查到的时候，给个初始值 1

        # 页数自增
        page_num += 1

    # 移除没有统计的任务状态数据
    temp_tatistics = copy.deepcopy(my_statistics)  # 深拷贝
    for key, value in temp_tatistics.items():
        if len(value.split(":")) == 1:
            removed_value = my_statistics.pop(key)  # 移除 'key' 及其对应的值，并返回被移除的值

    error_tasks = 0
    for val in my_statistics.values():
        i, j = val.split(":")
        print(f"{i}\t{j}")
        error_tasks = int(j)        # 最后一个98 是”错题确认中“

    print(f"--------------------\n总计\t{statistics_total}-{error_tasks}={eval(str(statistics_total-error_tasks))} \n")


def get_question_status2(task_ids=None):
    """ 根据“题目ID”的集合，获取指定题目的状态，便于及时查询 """
    page_num, page_size, statistics_total = 1, 20, 0        # statistics_total 本次统计数量

    temp_results = []
    while True:
        params = {
            "pageNum": page_num,
            "pageSize": page_size,
            "taskStatusList": [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29,
                               30, 31, 32, 33, 34, 35, 95]
        }  # 98: "错题确认中" 排除统计范围
        task_data = get_request(task_interface, params=params)
        # print(task_data)

        # 如果已经找满了数据就开溜（但是中途可能会加入数据，所以尽可能在查询的时候先不要动后台）
        if statistics_total == task_data["total"]:
            break

        # 开始逐一分析数据
        for row in task_data["rows"]:
            statistics_total += 1

            task_id, task_status = row["questionId"], row["taskStatus"]  # 任务ID、任务状态
            if str(task_id) in task_ids:
                temp_results.append((str(task_id), task_status_dict[task_status]))

        # 页数自增
        page_num += 1

    """ 按照给的 task_ids 数组的顺序进行排序后再输出 """
    results = []
    for task_id in task_ids:
        is_find = False
        for res in temp_results:
            if task_id == res[0]:
                results.append(res)
                is_find = True
                break

        # 如果没有查询到，那就空着
        if not is_find:
            results.append((str(task_id), ""))

    return results      # [("task_id", "task_status", "task_status_name"), ("task_id", "task_status", "task_status_name")]


if __name__ == "__main__":
    """ 登录获取 token """
    post_data = {
        "username": "z",
        "password": "5f1",
        "code": "0",  # TODO
        "uuid": "e5639e5bcfc142af807e1a72fd94bb19"  # data_dict["uuid"]     # TODO
    }

    login_data = post_request(login_interface, **post_data)

    token = login_data["token"]
    print(f"token:\n{token}\n")
    post_headers(token)  # headers 加入 token
    # print(get_headers())

    """ 统计全部”已完成“题目状态数量 """
    get_question_status1()

    """ 统计具体“题号ID集合”的题目状态，题目集合放在 task_ids.txt """
    task_ids = get_array()
    tasks = get_question_status2(task_ids=task_ids)
    for task in tasks:
        task_id, task_status = task
        print(f"{task_id}\t{task_status}")


