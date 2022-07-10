import requests

# 参数请求
# 定义url
base_url = 'http://httpbin.org'

# 定义需要传的参数
param_date = {'user': 'zhang',
              'pasword': '123456'}
# get方法的使用
r = requests.get(base_url + '/get', params=param_date)
print(r.url)
print(r.status_code)
