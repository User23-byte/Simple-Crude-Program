from flask import Flask,render_template
from example import get_connection

app=Flask(__name__)

@app.route("/")
def index():
    connection=get_connection()
    with connection.cursor() as cur:
        sql_stmt="SELECT * FROM student"
        cur.execute(sql_stmt)
        res=cur.fetchall()
        print(res)
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
    
