'''
Author: shgopher shgopher@gmail.com
Date: 2024-09-03 23:24:47
LastEditors: shgopher shgopher@gmail.com
LastEditTime: 2024-09-03 23:33:22
FilePath: /PythonFamily/web/django/static.py
Description: 

Copyright (c) 2024 by shgopher, All Rights Reserved. 
'''
import os
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

# 设置 Django 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', './settings.py')

# 获取 Django 的 WSGI 应用对象
application = get_wsgi_application()

def serve_static(request, path):
    full_path = os.path.join(settings.STATIC_ROOT, path)
    if os.path.exists(full_path):
        with open(full_path, 'rb') as f:
            content = f.read()
        return HttpResponse(content, content_type='application/octet-stream')
    else:
        return HttpResponse(status=404)

urlpatterns = [
    path('static/<path:path>', serve_static),
]