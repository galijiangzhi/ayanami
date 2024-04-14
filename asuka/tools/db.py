import pymysql

# 定义一个函数来执行查询
def execute_query(reque_data):
    # 连接到数据库
    conn = pymysql.connect(host='192.168.31.100', user='root', password='viekk2423', database='eva')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute(reque_data)
    rows = cursor.fetchall()

    # 遍历结果
    for row in rows:
        print(row)

    # 关闭连接
    cursor.close()
    conn.close()
    return rows[0]