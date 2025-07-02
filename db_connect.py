import mariadb
try:
    connect=mariadb.connect(
        user="Aayusha",
        password="pass1",
        host="",
        port=3306,
        database="schooldb"
    )
except Exception as e:
    print(f"Error: {e}")

# cur=connect.cursor()
# cur.execute("update student set student_email="jane@gmail.com" where id=6")
# cur.execute("commit")
# # res=cur.fetchall()
# # for item in res:
# #     print(item)
# #cur.execute("commit")