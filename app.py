from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
db = SQLAlchemy(app)

class Record(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Daily_Record"
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal = db.Column(db.String(50), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    achievement = db.Column(db.Integer, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False)
    # due = db.Column(db.DateTime, nullable=False) #必須項目


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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        goal = Mandala.query.all()
        goal = Record.query.all()
        print(goal)
        return render_template("index.html", posts = goal)

@app.route("/create", methods=['GET', 'POST'])
def create():
    # リクエストがGETのとき
    if request.method == "GET":
        # posts = Record.query.all()
        return render_template("create.html")

    else:
        goal = request.form.get("goal")
        detail = request.form.get("detail")
        achievement = request.form.get("achievement")
        create_at = request.form.get("create_at")
        create_at = datetime.strptime(create_at, "%Y-%m-%d")

        new_post = Record(goal=goal, detail=detail, achievement=achievement, create_at=create_at)
        db.session.add(new_post)
        db.session.commit()

        return redirect('/detail')

@app.route('/detail')
def read():
    posts = Record.query.order_by(Record.create_at).all()
    return render_template('detail.html', posts=posts, today=date.today())

@app.route('/detail/task/<int:id>')
def read_task(id):
    post=Record.query.get(id)
    return render_template("task.html", post=post)

@app.route('/detail/update/<int:id>', methods=['GET', 'POST'])
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
def create_mandala():
    # post = Record.query.get(id)
    if request.method == "GET":
        return render_template("create_mandala.html")
    else:
        db.session.commit()

        return redirect("/")

# JSのフェッチするときに指定するURLのために、新しく用意したもの
@app.route("/create_mandala/get", methods=["GET", "POST"])
def create_mandala_test():
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

if __name__ == "__main__":
    app.run(debug=True)