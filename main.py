# -*- coding: utf-8 -*-
from flask import Flask,request,session
from serverless import create_environ, get_response, wrap_response

path_reserved="/sample_path"
#api网关触发器中访问路径自带的前缀
#例如https://service-*******.ap-shanghai.apigateway.myqcloud.com/release/sample_path
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def index():
    return "Hello World"

def main_handler(event, context):
    environ = create_environ(event, context,path_reserved)
    response = get_response(app, environ)
    return wrap_response(response)

if __name__ == '__main__':
    app.run()
