from pymysql import connect
def main():
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs=conn.cursor()
    cont=cs.execute('''select * from 数据表''')
    cs.close()
    conn.close()