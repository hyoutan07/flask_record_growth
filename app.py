from typing import get_args
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
db = SQLAlchemy(app)

class Record(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Diry_Record"
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal = db.Column(db.String(50), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    achievement = db.Column(db.Integer, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False)

class Mandala(db.Model):
    # テーブルの名前の設定
    __tablename__ = "Mandala_Chart"
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal_main = db.Column(db.String(50), nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
    # リクエストがGETのとき
    if request.method == "GET":
        goal = Mandala.query.all()
        return render_template("index.html", posts = goal)
    
    elif request.method == "POST":
        goal = request.form.get("goal")
        detail = request.form.get("detail")
        achievement = request.form.get("achievement")
        create_at = request.form.get("create_at")
        create_at = datetime.strptime(create_at, "%Y-%m-%d")

        new_post = Record(goal=goal, detail=detail, achievement=achievement, create_at=create_at)
        db.session.add(new_post)
        db.session.commit()

        return redirect("/")


@app.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")

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


if __name__ == "__main__":
    app.run(debug=True)