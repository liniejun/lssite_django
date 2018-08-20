#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Brief
# @Version 1.0
# @Date
#
#
__author__ = 'Shawn Lee'

import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
# 第一个参数是邮件主题subject；
# 第二个参数是邮件具体内容；
# 第三个参数是邮件发送方，需要和你settings中的一致；
# 第四个参数是接受方的邮件地址列表。
# 请按你自己实际情况修改发送方和接收方的邮箱地址。

#     send_mail(
#         '来自xxx.com的测试邮件',
#         '欢迎访问xxx，本站专注于Python和Django技术的分享！',
#         'xxx@sina.com',
#         ['xxx@qq.com'],
#     )

    subject, from_email, to = '来自xxxx.com的测试邮件', 'xxx@sina.com', 'xxx@qq.com'
    text_content = '欢迎访问xxx.com,专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://xxx.com" target=blank>xxx.com</a>，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()