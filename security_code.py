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
  date        : 2024/5/7 19:25
-------------------------------------------------
"""
from common import get_request, captcha_image_interface


if __name__ == "__main__":
    data_dict = get_request(captcha_image_interface)
    yanzhengma = "data:image/gif;base64," + data_dict["img"]  # 验证码

    print(data_dict["uuid"], data_dict["img"])

