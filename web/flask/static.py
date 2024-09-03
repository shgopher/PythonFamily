'''
Author: shgopher shgopher@gmail.com
Date: 2024-09-03 23:36:41
LastEditors: shgopher shgopher@gmail.com
LastEditTime: 2024-09-03 23:37:08
FilePath: /PythonFamily/web/flask/static.py
Description: 

Copyright (c) 2024 by shgopher, All Rights Reserved. 
'''
from flask import Flask, send_from_directory

app = Flask(__name__)

# 指定静态文件目录
static_folder = 'your_static_folder_path'

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_folder, filename)

if __name__ == '__main__':
    app.run()