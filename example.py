import mariadb

from dotenv import load_dotenv
import os 

load_dotenv()
def get_connection():
    try:
        connection =mariadb.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=3306 ,
            database=os.getenv('DB_NAME')
        )
        return connection
    except Exception as e:
        print(f"Unable to create database connection :{e}")


# print(connection)
# cur=connection.cursor()
# sql_query="select * from student where id=4"
# cur.execute(sql_query)
# # cur.execute("commit")
# res= cur.fetchall()
# print(res)