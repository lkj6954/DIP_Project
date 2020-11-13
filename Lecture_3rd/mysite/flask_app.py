from flask import Flask, render_template, request   # render_template == return으로 파일을 가져올 때 쓰는 lib
import pymysql
import time
import os

# 시간을 한국으로 설정
os.environ["TZ"] = "Asia/Seoul"
time.tzset()

app = Flask(__name__)

@app.route('/', methods=["GET","POST"]) # GET, POST 통신 둘 다 쓰겠다는 의미
def hello_world():
    if request.method == 'GET' :
        return render_template('index.html')
    else :  # POST 방식의 요청
        # python에서 통신은 requests이지만 flask에서는 request이다.
        subject = request.form['subject'] # '/'페이지의 form 태그 안에 있는 subject 값과 content 값을 받아 넣는다.
        content = request.form['content']
        dbconn = pymysql.connect(
            host = 'rltkwpdntm.mysql.pythonanywhere-services.com', # host : rltkwpdntm.mysql.pythonanywhere-services.com
            port = 3306,
            user = 'rltkwpdntm',
            passwd = 'SicParvisMagna',
            db = 'rltkwpdntm$default',
            charset = 'utf8'
        )
        cursor = dbconn.cursor()    # MySQL 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져옴
        sql = "insert into board set subject = '%s', content = '%s'; " % (subject, content) # SQL Insert
        cursor.execute(sql)         # Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 전송
        dbconn.commit()             # DML 문장을 실행하는 경우, insert,update,delete 후 Connection 객체의 commit() 메서드를 사용해서 데이터를 확정

        return render_template('index.html', subject=subject, content=content) # render_template로 index.html를 리턴할 때 플라스크에서 받은 subject 값과 content 값도 전달하는 것

@app.route('/iot', methods=["GET", "POST"])
def iot():
    if request.method == 'GET':         # 서버주소/iot로 GET 요청이 들어오면
        pir = request.args.get('pir')   # GET 방식으로 받을 때는 request. 가 아닌 request.args.get 으로 해야 됨
        indate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        dbconn = pymysql.connect(
            host = 'rltkwpdntm.mysql.pythonanywhere-services.com', # host : rltkwpdntm.mysql.pythonanywhere-services.com
            port = 3306,
            user = 'rltkwpdntm',
            passwd = 'SicParvisMagna',
            db = 'rltkwpdntm$default',
            charset = 'utf8'
        )
        cursor = dbconn.cursor()
        sql = "insert into iot set pir = '%s', indate = '%s'; " % (pir, indate)
        cursor.execute(sql)
        dbconn.commit()
    return "ok"