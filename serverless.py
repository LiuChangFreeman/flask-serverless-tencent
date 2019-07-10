# -*- coding: utf-8 -*-
import sys
if sys.version_info.major == 2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode  
from werkzeug.wrappers import BaseResponse

def create_environ(event, context,trim):
    method = event['httpMethod'] if 'httpMethod' in event else 'GET'
    path = event['path'] if 'path' in event else '/'
    path =path.replace(trim,"")
    query = event['queryString'] if 'queryString' in event else {}
    query_string = urlencode(query, True)
    headers = event['headers'] if 'headers' in event else {}
    server_name = headers['host'] if 'host' in headers else '127.0.0.1'
    body = event['body'] if 'body' in event else ''
    request_context = event['requestContext'] if 'requestContext' in event else {}
    remote_addr = request_context.get('sourceIp', '127.0.0.1')
    environ = {
        'PATH_INFO': path,
        'QUERY_STRING': query_string,
        'REMOTE_ADDR': remote_addr,
        'REQUEST_METHOD': method,
        'SCRIPT_NAME': '',
        'SERVER_NAME': server_name,
        'SERVER_PORT': 80,
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'SERVER_SOFTWARE': 'serverlessplus',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'http',
        'wsgi.input': body,
        'wsgi.errors': sys.stderr,
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
    }
    for name, value in headers.items():
        canonical_name = "HTTP_{}".format(name.upper().replace('-', '_'))
        environ[canonical_name] = value
    return environ

def get_response(app, environ):
    return BaseResponse.from_app(app, environ)

def wrap_response(response):
    headers = {}
    for name, value in response.headers:
        headers[name] = value
    wrapped_response={
        "isBase64Encoded": False,
        "statusCode": response.status_code,
        "headers": headers,
        "body": response.data.decode("utf-8")
    }
    return wrapped_response
