from email import message
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flask import jsonify
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

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

# ここの内容を変更する
class Mandala(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Mandala_Chart"
    id = db.Column(db.Integer, primary_key=True) #主キー
    # goal_main = db.Column(db.String(50), primry_key=True, nullable=True)
    column_11 = db.Column(db.String(50), nullable=True)
    column_12 = db.Column(db.String(50), nullable=True)
    column_13 = db.Column(db.String(50), nullable=True)
    column_14 = db.Column(db.String(50), nullable=True)
    column_15 = db.Column(db.String(50), nullable=True)
    column_16 = db.Column(db.String(50), nullable=True)
    column_17 = db.Column(db.String(50), nullable=True)
    column_18 = db.Column(db.String(50), nullable=True)
    column_19 = db.Column(db.String(50), nullable=True)

    column_21 = db.Column(db.String(50), nullable=True)
    column_22 = db.Column(db.String(50), nullable=True)
    column_23 = db.Column(db.String(50), nullable=True)
    column_24 = db.Column(db.String(50), nullable=True)
    column_25 = db.Column(db.String(50), nullable=True)
    column_26 = db.Column(db.String(50), nullable=True)
    column_27 = db.Column(db.String(50), nullable=True)
    column_28 = db.Column(db.String(50), nullable=True)
    column_29 = db.Column(db.String(50), nullable=True)

    column_31 = db.Column(db.String(50), nullable=True)
    column_32 = db.Column(db.String(50), nullable=True)
    column_33 = db.Column(db.String(50), nullable=True)
    column_34 = db.Column(db.String(50), nullable=True)
    column_35 = db.Column(db.String(50), nullable=True)
    column_36 = db.Column(db.String(50), nullable=True)
    column_37 = db.Column(db.String(50), nullable=True)
    column_38 = db.Column(db.String(50), nullable=True)
    column_39 = db.Column(db.String(50), nullable=True)

    column_41 = db.Column(db.String(50), nullable=True)
    column_42 = db.Column(db.String(50), nullable=True)
    column_43 = db.Column(db.String(50), nullable=True)
    column_44 = db.Column(db.String(50), nullable=True)
    column_45 = db.Column(db.String(50), nullable=True)
    column_46 = db.Column(db.String(50), nullable=True)
    column_47 = db.Column(db.String(50), nullable=True)
    column_48 = db.Column(db.String(50), nullable=True)
    column_49 = db.Column(db.String(50), nullable=True)

    column_51 = db.Column(db.String(50), nullable=True)
    column_52 = db.Column(db.String(50), nullable=True)
    column_53 = db.Column(db.String(50), nullable=True)
    column_54 = db.Column(db.String(50), nullable=True)
    column_55 = db.Column(db.String(50), nullable=True)
    column_56 = db.Column(db.String(50), nullable=True)
    column_57 = db.Column(db.String(50), nullable=True)
    column_58 = db.Column(db.String(50), nullable=True)
    column_59 = db.Column(db.String(50), nullable=True)

    column_61 = db.Column(db.String(50), nullable=True)
    column_62 = db.Column(db.String(50), nullable=True)
    column_63 = db.Column(db.String(50), nullable=True)
    column_64 = db.Column(db.String(50), nullable=True)
    column_65 = db.Column(db.String(50), nullable=True)
    column_66 = db.Column(db.String(50), nullable=True)
    column_67 = db.Column(db.String(50), nullable=True)
    column_68 = db.Column(db.String(50), nullable=True)
    column_69 = db.Column(db.String(50), nullable=True)

    column_71 = db.Column(db.String(50), nullable=True)
    column_72 = db.Column(db.String(50), nullable=True)
    column_73 = db.Column(db.String(50), nullable=True)
    column_74 = db.Column(db.String(50), nullable=True)
    column_75 = db.Column(db.String(50), nullable=True)
    column_76 = db.Column(db.String(50), nullable=True)
    column_77 = db.Column(db.String(50), nullable=True)
    column_78 = db.Column(db.String(50), nullable=True)
    column_79 = db.Column(db.String(50), nullable=True)

    column_81 = db.Column(db.String(50), nullable=True)
    column_82 = db.Column(db.String(50), nullable=True)
    column_83 = db.Column(db.String(50), nullable=True)
    column_84 = db.Column(db.String(50), nullable=True)
    column_85 = db.Column(db.String(50), nullable=True)
    column_86 = db.Column(db.String(50), nullable=True)
    column_87 = db.Column(db.String(50), nullable=True)
    column_88 = db.Column(db.String(50), nullable=True)
    column_89 = db.Column(db.String(50), nullable=True)

    column_91 = db.Column(db.String(50), nullable=True)
    column_92 = db.Column(db.String(50), nullable=True)
    column_93 = db.Column(db.String(50), nullable=True)
    column_94 = db.Column(db.String(50), nullable=True)
    column_95 = db.Column(db.String(50), nullable=True)
    column_96 = db.Column(db.String(50), nullable=True)
    column_97 = db.Column(db.String(50), nullable=True)
    column_98 = db.Column(db.String(50), nullable=True)
    column_99 = db.Column(db.String(50), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ユーザー設定
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25))
    record = db.relationship("Record", backref = "user", lazy = "joined", cascade = "delete")
    mandala = db.relationship("Mandala", backref = "user", lazy = "joined", cascade = "delete")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    messages = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user:
            messages += "name already exists"
            return render_template("signup.html",messages = messages)


        user = User(username = username, password = generate_password_hash(password, method="sha256"))
        db.session.add(user)
        db.session.flush()

        new_mandala = Mandala(goal_main = "テスト")
        db.session.add(new_mandala)
        db.session.flush()

        user.mandala = [new_mandala]
        db.session.flush()

        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    global username
    messages = ""
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        user = User.query.filter_by(username=username).first()
        if user == None:
            messages += "name not found"
            return render_template("login.html",messages = messages)

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
        else:
            messages += "password is wrong"
            return render_template("login.html",messages = messages)
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
    tmp = user.record
    # posts = tmp.query.order_by(tmp.create_at).all()
    return render_template('detail.html', posts=tmp, today=date.today())

@app.route('/detail/task/<int:id>')
@login_required
def read_task(id):
    post=Record.query.get(id)
    return render_template("task.html", post=post)

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
    # post = Record.query.get(id)
    if request.method == "GET":
        return render_template("create_mandala.html")
    else:
        db.session.commit()

        return redirect("/")

# JSのフェッチするときに指定するURLのために、新しく用意したもの
@app.route("/create_mandala/get", methods=["GET", "POST"])
@login_required
def create_mandala_test():
    user = User.query.filter_by(username=username).first()
    mandala = user.mandala[0]
    mandala_test = Mandala.query.get(1)

    print(mandala)
    print(mandala_test)

    if request.method == "GET":
        result = {"title":"Pythonから送ったよ"}
        print(result)
        return jsonify(result)

    if request.method == "POST":
        data = request.get_json()

        print("aaa\n")
        print(data["message"]),

        print(data["column_11"]),
        print(data["column_12"]),
        print(data["column_13"]),
        print(data["column_14"]),
        print(data["column_15"]),
        print(data["column_16"]),
        print(data["column_17"]),
        print(data["column_18"]),
        print(data["column_19"]),

        print(data["column_21"]),
        print(data["column_22"]),
        print(data["column_23"]),
        print(data["column_24"]),
        print(data["column_25"]),
        print(data["column_26"]),
        print(data["column_27"]),
        print(data["column_28"]),
        print(data["column_29"]),

        print(data["column_31"]),
        print(data["column_32"]),
        print(data["column_33"]),
        print(data["column_34"]),
        print(data["column_35"]),
        print(data["column_36"]),
        print(data["column_37"]),
        print(data["column_38"]),
        print(data["column_39"]),

        print(data["column_41"]),
        print(data["column_42"]),
        print(data["column_43"]),
        print(data["column_44"]),
        print(data["column_45"]),
        print(data["column_46"]),
        print(data["column_47"]),
        print(data["column_48"]),
        print(data["column_49"]),

        print(data["column_51"]),
        print(data["column_52"]),
        print(data["column_53"]),
        print(data["column_54"]),
        print(data["column_55"]),
        print(data["column_56"]),
        print(data["column_57"]),
        print(data["column_58"]),
        print(data["column_59"]),

        print(data["column_61"]),
        print(data["column_62"]),
        print(data["column_63"]),
        print(data["column_64"]),
        print(data["column_65"]),
        print(data["column_66"]),
        print(data["column_67"]),
        print(data["column_68"]),
        print(data["column_69"]),

        print(data["column_71"]),
        print(data["column_72"]),
        print(data["column_73"]),
        print(data["column_74"]),
        print(data["column_75"]),
        print(data["column_76"]),
        print(data["column_77"]),
        print(data["column_78"]),
        print(data["column_79"]),

        print(data["column_81"]),
        print(data["column_82"]),
        print(data["column_83"]),
        print(data["column_84"]),
        print(data["column_85"]),
        print(data["column_86"]),
        print(data["column_87"]),
        print(data["column_88"]),
        print(data["column_89"]),

        print(data["column_91"]),
        print(data["column_92"]),
        print(data["column_93"]),
        print(data["column_94"]),
        print(data["column_95"]),
        print(data["column_96"]),
        print(data["column_97"]),
        print(data["column_98"]),
        print(data["column_99"]),

        success = {"success":"成功したよ！"}
        return jsonify(success)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)