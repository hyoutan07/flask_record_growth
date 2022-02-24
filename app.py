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
    goal_main = db.Column(db.String(50), nullable=False)

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