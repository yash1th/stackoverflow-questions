import json
import requests
response = requests.get('http://fundgz.1234567.com.cn/js/110022.js?rt=0.5198424438182809')
print(response)
ret = json.loads(response.content.decode('utf-8'))
print(ret)