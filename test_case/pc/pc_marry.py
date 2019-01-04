#1.设置条件；2.解析网页；3下载图片；4.保存信息
#http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=180&marry=1&page=1

import requests
import json

import os

#设置条件:年龄
def query_age():
    age=int(input("请输入对方的年龄(如22)："))
    if 21<=age<= 30:
        startage=21
        endage=30
    elif 31<=age<=40:
        startage=31
        endage=40
    #print (startage,endage)
    return startage,endage


#设置条件:性别
def query_sex():
    sex = input("请输入对方的性别(如女)：")
    if sex == '男':
        gender = 1
    else:
        gender = 2
    #print(gender)
    return gender


#设置条件：城市
def query_city():
    city=input("请输入城市名称：如武汉：")
    if city=='武汉':
        cityid = 180
    #print(cityid)
    return cityid




#查询符合条件的数据,把url的参数值放到一起，变量来接收返回
def query_data():
    print('请输入以下符合你条件的：')
    #年龄：
    startage, endage=query_age()                #对于返回的2个参数可以用2个变量来接收
    #性别
    gender=query_sex()
    #城市查询：
    cityid=query_city()
    # 获取10页的内容，10页22条
    for i in range(1, 11):
        json=get_one(i, startage, endage, gender, cityid)  # 把所有变量当参数都传递给函数get_one，把函数get_one返回的值用json来接收
        #print(json['data']['list'])

        for item in json['data']['list']:  #循环读取列表的值 for item in
            #print(item)
            sava_image(item)              #这个方法是保存图片到本地文件夹下
            save_info(item)               #这个方法是保存个人信息


#这个方法是保存图片到本地文件夹下
def sava_image(item):
    if not os.path.exists('images'):   #如果该路径下不存在一个叫images的文件夹就创建
        os.mkdir('images')
    image_url = item['avatar']     #用变量把列表下的图片路径接收，图片URL地址
    r=requests.get(image_url)     #在这个方法下发送图片的路径获取图片
    if r.status_code==200:
        file_path='images/{}.jpg'.format(item['username'])#请求成功的图片给放到images文件夹下的file_path路径里，并且以列表信息的人名来命名路径
        if not os.path.exists(file_path):
            print('正在获取%s的信息'%item['username'])
            with open(file_path,'wb')as f:                       #打开该路径文件，把图片内容写进去，图片只能用wb二进制来写
                f.write(r.content)
        else:
            print('已经保存过当前图片的信息了')



# 这个方法是保存个人信息
def save_info(item):
    with open('grilInfo/'+item['username']+'.txt','w',encoding='utf-8')as f:
        f.write('名字:'+item['username']+',城市：'+item['city'])






#接收下面获取到的参数值，拼接URL，请求返回json数据，，，拼接URL:http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=180&marry=1&page=1，用参数来进行拼接
def get_one(page,startage,endage,gender,cityid):
    headers={
        'Referer':'http://www.7799520.com/jiaoyou.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    base_url='http://www.7799520.com/api/user/pc/list/search?startage={}&endage={}&gender={}&cityid={}&marry=1&page={}'.format(startage,endage,gender,cityid,page)#拼接URL
    print(base_url)
    while True:#死循环请求
        try:
            response=requests.get(base_url,headers=headers)  #get 请求后可以直接打印r.json()
            #print(response)
            if response.status_code == 200:
                print(response.json())  #返回正确的json数据
                return response.json()
        except:
            return None


data = query_data()

