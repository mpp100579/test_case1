import pandas as pd
import cx_Oracle
# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#实现查询并返回dataframe
#实现查询操作
def query(table):
    host = "192.168.1.56"    #数据库ip
    port = "1521"     #端口
    sid = "bkcyun"    #数据库名称
    dsn = cx_Oracle.makedsn(host, port, sid)

    #scott是数据用户名，tiger是登录密码（默认用户名和密码）
    conn = cx_Oracle.connect("bkcyun", "bkc123456", dsn)

    #SQL语句，可以定制，实现灵活查询
    sql = 'select * from '+ table

    # 使用pandas 的read_sql函数，可以直接将数据存放在dataframe中
    results = pd.read_sql(sql,conn)
    conn.close
    return results
test_data = query('SYSUSER') # 可以得到结果集
print (test_data)


#数据库插入操作：
import pandas as pd

import cx_Oracle
dict={
    'name':['张三','李四','王五','赵六'],
    'sex':['男','女','男','女'],
    'age':[18,19,20,21]
}
pf=pd.DataFrame(dict)
print (pf)


# 实现插入功能
def input_to_db(data, table):
    host = "192.168.1.56"  # 数据库ip
    port = "1521"  # 端口
    sid = "bkcyun"  # 数据库名称
    dsn = cx_Oracle.makedsn(host, port, sid)

    # scott是数据用户名，tiger是登录密码（默认用户名和密码）
    conn = cx_Oracle.connect("bkcyun", "bkc123456", dsn)

    # 建立游标
    cursor = conn.cursor()

    # sql语句,注意%s要加引号，否则会报ora-01036错误
    query = "INSERT INTO" + table + "(ID, NAME , PHONE, ADRRESSS) values (%d, %s, %s, %s)"
    # 逐行插入数据
    for i in range(len(data)):
        name = data.ix[i, 0]
        gender = data.ix[i, 1]
        age = data.ix[i, 2]

        # 执行sql语句
        cursor.execute(query %(id, 'name',phone, 'adrress'))
        connection.commit()

        # 关闭游标
        cursor.close()
        connection.close()

        # 测试插入数据库
        # 测试数据集
        test_data = pd.DataFrame([[11,'app1', 123, '哈三电厂1'], [12, 'app2',124,'哈三电厂2']], index=[1, 2], columns=['ID', 'NAME' , 'PHONE', 'ADRRESSS'])

# 调用函数实现插入
input_to_db(test_data,table='contacts')