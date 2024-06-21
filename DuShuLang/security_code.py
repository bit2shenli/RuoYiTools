# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : id_code
  Description : 在线base64转图片工具：
                https://onlinetools.com/image/convert-base64-to-image

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/6/20 19:25
-------------------------------------------------
"""
from common import post_request, captcha_image_interface

if __name__ == "__main__":
    post_data = {}
    login_data = post_request(captcha_image_interface, **post_data)

    if login_data["code"] == 0:
        data = login_data["data"]
        captcha_id = data["captchaId"]
        image = data["picPath"]
        print(captcha_id, image)