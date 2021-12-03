from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////record.db"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    achievement = db.Column(db.Integer, nullable=True)
    today = db.Column(db.DateTime, nullable=False)



@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)