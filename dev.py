from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    data = get_main_data()

    labels = []
    value = []
    for item in data:
        labels.append(item[1])
        value.append(item[2])

    return render_template('home.html', headquaters=labels, data=value)

@app.route('/sido/<int:sido_id>')
def show_detail(sido_id):

    data = get_sub_data(sido_id)

    print(data)

    return render_template('detail.html', data=data)

def get_main_data():
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  'SELECT * FROM main'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data

def get_sub_data(sido_id):
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  f'SELECT * FROM sub_table WHERE id = {sido_id + 1}'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data.fetchone()
    
if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True)