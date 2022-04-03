from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flask import jsonify
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import desc
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Record(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Daily_Record"
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal = db.Column(db.String(50), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    achievement = db.Column(db.Integer, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False)
    # due = db.Column(db.DateTime, nullable=False) #必須項目
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# # 新しく追加した箇所
# ENGINE = create_engine(
#     Record,
#     encoding = "utf-8",
#     echo=True # Trueだと実行のたびにSQLが出力される
# )
# # Sessionの作成
# session = scoped_session(
#   # ORM実行時の設定。自動コミットするか、自動反映するなど。
#     sessionmaker(
#         autocommit = False,
#         autoflush = False,
#         bind = ENGINE
#         )
# )


# ここの内容を変更する
class Mandala(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Mandala_Chart"
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal_main = db.Column(db.String(50), nullable=False)

# ユーザー設定
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25))
    record = db.relationship("Record", backref = "user", lazy = "joined", cascade = "delete")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User(username = username, password = generate_password_hash(password, method="sha256"))
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    global username
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user = User.query.filter_by(username=username).first()
    # print(user.record[0].create_at)
    print()
    if request.method == "GET":
        goal = Mandala.query.all()
        goal = Record.query.all()
        print(goal)
        print(user.record)
        print(type(user.record))
        return render_template("index.html", posts = goal, username = user.username, userrecord = user.record)

@app.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    user = User.query.filter_by(username=username).first()

    print(user)
    # リクエストがGETのとき
    if request.method == "GET":
        return render_template("create.html")

    else:
        goal = request.form.get("goal")
        detail = request.form.get("detail")
        achievement = request.form.get("achievement")
        create_at = request.form.get("create_at")
        create_at = datetime.strptime(create_at, "%Y-%m-%d")

        new_record = Record(goal=goal, detail=detail, achievement=achievement, create_at=create_at)
        # goal = Record.query.all()
        # print(goal)
        db.session.add(new_record)
        db.session.flush()

        user.record += [new_record]

        db.session.flush()
        db.session.commit()
        print(type(user.record))
        return redirect('/detail')


@app.route('/detail')
@login_required
def read():
    user = User.query.filter_by(username=username).first()
    posts = user.record  
    
    # 今日の記録のリセット用
    for i in range(len(posts)):
        for j in range(len(posts)-1, i, -1):
            if posts[j].create_at > posts[j-1].create_at:
                posts[j].create_at,  posts[j-1].create_at = posts[j-1].create_at, posts[j].create_at
    

    return render_template('detail.html', posts=posts, today=date.today())

""" インデックス番号順に検索をかけて挿入個所を決める """


@app.route('/detail/task/<int:id>')
@login_required
def read_task(id):
    post=Record.query.get(id)
    user = User.query.filter_by(username=username).first()
    posts = user.record

    # 今日の記録のリセット用
    for i in range(len(posts)):
        for j in range(len(posts)-1, i, -1):
            if posts[j].create_at > posts[j-1].create_at:
                posts[j].create_at,  posts[j-1].create_at = posts[j-1].create_at, posts[j].create_at

    return render_template("task.html", post=post, posts=posts)

@app.route('/detail/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    post = Record.query.get(id)


    if request.method == 'GET':

        return render_template('update.html', post=post)    
    else:
        post.goal = request.form.get('goal')
        post.detail = request.form.get('detail')
        post.create_at = datetime.strptime(request.form.get('create_at'), '%Y-%m-%d')

        db.session.commit()

        return redirect('/detail')


@app.route("/create_mandala", methods=["GET", "POST"])
@login_required
def create_mandala():
    if request.method == "GET":
        return render_template("create_mandala.html")
    elif request.method == "POST":
        goal_main = request.form.get("goal_main")

        new_post = Mandala(goal_main = goal_main)

        db.session.add(new_post)
        db.session.commit()

        return redirect("/")

# JSのフェッチするときに指定するURLのために、新しく用意したもの
@app.route("/create_mandala/get", methods=["GET", "POST"])
@login_required
def create_mandala_test():
    if request.method == "GET":
        result = {"title":"Pythonから送ったよ"}
        print(result)
        return jsonify(result)

    if request.method == "POST":
        print("aaa")
        print(request.get_json())
        success = {"success":"成功したよ！"}
        return jsonify(success)

if __name__ == "__main__":
    app.run(debug=True)