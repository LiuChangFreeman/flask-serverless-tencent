# flask-serverless-tencent
专供腾讯云SCF使用，支持Python2.7与3.6的Flask框架的API网关触发器转接库，您只需要将serverless.py拷贝到Flask项目根目录即可。

简单的三步即可将Flask适配到SCF环境中。

# 1、在Flask应用中引入serverless.py 
```
from flask import Flask,request,session
from serverless import create_environ, get_response, wrap_response
app = Flask(__name__)
```

# 2、使用serverless.py创建SCF主函数入口
```
def main_handler(event, context):
    environ = create_environ(event, context,path_reserved)
    response = get_response(app, environ)
    return wrap_response(response)
```

# 3、修改API网关触发器的路径前缀

```
path_reserved="/sample_path"
#api网关触发器中访问路径自带的前缀
```

以上为此示例访问路径的修改方法:...apigateway.myqcloud.com/release/`sample_path`
