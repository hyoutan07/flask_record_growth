from typing import get_args
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True) #主キー
    goal = db.Column(db.String(50), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    achievement = db.Column(db.Integer, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False)
    # due = db.Column(db.DateTime, nullable=False) #必須項目

@app.route('/')
def index():
    return render_template('index.html')

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

        return redirect('/')

@app.route('/detail')
def read():
    posts = Record.query.order_by(Record.create_at).all()
    return render_template('detail.html', posts=posts, today=date.today())

if __name__ == "__main__":
    app.run(debug=True)