import pymysql.cursors

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='students',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        sql = "SELECT id, firstname, lastname FROM users"
        cursor.execute(sql)

        rows = cursor.fetchall()

        if not rows:
            print("No data found.")
        else:
            for row in rows:
                print("firstname :", row["firstname"])
                print("lastname :", row["lastname"])
                print("------------------")

except Exception as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()