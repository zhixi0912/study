from pymysql import Connection

conn = Connection(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root1234"
)

print(conn.get_server_info())

conn.close()