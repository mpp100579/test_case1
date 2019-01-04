import unittest       #导入unittest
import requests     #导入requests库
import json            #导入json

class LianXi(unittest.TestCase):              #定义一个类，类的首字母要大写哦
       def setUp(self):                                 #初始化
             self.base_url = 'http://192.168.1.15/'

       def test_get_success(self):             #定义一个方法，切记要以test开头哦
             datalist = {'用户名': 'yujian', '密码': 'Bkc123456'}               #定义传参数据
             head = {"Content-Type": "application/Json"}     #定义头部
             r = requests.post(self.base_url, params=datalist, headers=head)          #传入参数
             result = json.loads(r.text)            #使用json格式返回
             self.assertEqual(result['status'], 0)      #检验返回值
             print(result)
             print('get请求获取的响应结果json类型', r.text)
             print("get请求获取响应状态码", r.status_code)
             print("get请求获取响应头", r.headers['Content-Type'])

        # 响应的json数据转换为可被python识别的数据类型 15 json_r = r.json() 16 print(json_r)
if __name__ == '__main__':
      unittest.main()
