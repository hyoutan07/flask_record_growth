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
    column_00 = db.Column(db.String(50),  nullable=True)

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
    mandala_test = Mandala.query.get(1)

    if request.method == "GET":
        result = {"column_00": mandala_test.column_00,
                  "column_11": mandala_test.column_11,
                  "column_12": mandala_test.column_12,
                  "column_13": mandala_test.column_13,
                  "column_14": mandala_test.column_14,
                  "column_15": mandala_test.column_15,
                  "column_16": mandala_test.column_16,
                  "column_17": mandala_test.column_17,
                  "column_18": mandala_test.column_18,
                  "column_19": mandala_test.column_19,

                  "column_21": mandala_test.column_21,
                  "column_22": mandala_test.column_22,
                  "column_23": mandala_test.column_23,
                  "column_24": mandala_test.column_24,
                  "column_25": mandala_test.column_25,
                  "column_26": mandala_test.column_26,
                  "column_27": mandala_test.column_27,
                  "column_28": mandala_test.column_28,
                  "column_29": mandala_test.column_29,   

                  "column_31": mandala_test.column_31,
                  "column_32": mandala_test.column_32,
                  "column_33": mandala_test.column_33,
                  "column_34": mandala_test.column_34,
                  "column_35": mandala_test.column_35,
                  "column_36": mandala_test.column_36,
                  "column_37": mandala_test.column_37,
                  "column_38": mandala_test.column_38,
                  "column_39": mandala_test.column_39,   

                  "column_41": mandala_test.column_41,
                  "column_42": mandala_test.column_42,
                  "column_43": mandala_test.column_43,
                  "column_44": mandala_test.column_44,
                  "column_45": mandala_test.column_45,
                  "column_46": mandala_test.column_46,
                  "column_47": mandala_test.column_47,
                  "column_48": mandala_test.column_48,
                  "column_49": mandala_test.column_49,   

                  "column_51": mandala_test.column_51,
                  "column_52": mandala_test.column_52,
                  "column_53": mandala_test.column_53,
                  "column_54": mandala_test.column_54,
                  "column_55": mandala_test.column_55,
                  "column_56": mandala_test.column_56,
                  "column_57": mandala_test.column_57,
                  "column_58": mandala_test.column_58,
                  "column_59": mandala_test.column_59,   

                  "column_61": mandala_test.column_61,
                  "column_62": mandala_test.column_62,
                  "column_63": mandala_test.column_63,
                  "column_64": mandala_test.column_64,
                  "column_65": mandala_test.column_65,
                  "column_66": mandala_test.column_66,
                  "column_67": mandala_test.column_67,
                  "column_68": mandala_test.column_68,
                  "column_69": mandala_test.column_69,   

                  "column_71": mandala_test.column_71,
                  "column_72": mandala_test.column_72,
                  "column_73": mandala_test.column_73,
                  "column_74": mandala_test.column_74,
                  "column_75": mandala_test.column_75,
                  "column_76": mandala_test.column_76,
                  "column_77": mandala_test.column_77,
                  "column_78": mandala_test.column_78,
                  "column_79": mandala_test.column_79,   

                  "column_81": mandala_test.column_81,
                  "column_82": mandala_test.column_82,
                  "column_83": mandala_test.column_83,
                  "column_84": mandala_test.column_84,
                  "column_85": mandala_test.column_85,
                  "column_86": mandala_test.column_86,
                  "column_87": mandala_test.column_87,
                  "column_88": mandala_test.column_88,
                  "column_89": mandala_test.column_89,

                  "column_91": mandala_test.column_91,
                  "column_92": mandala_test.column_92,
                  "column_93": mandala_test.column_93,
                  "column_94": mandala_test.column_94,
                  "column_95": mandala_test.column_95,
                  "column_96": mandala_test.column_96,
                  "column_97": mandala_test.column_97,
                  "column_98": mandala_test.column_98,
                  "column_99": mandala_test.column_99,

                  }
        print(result)
        return jsonify(result)

    if request.method == "POST":

        data = request.get_json()

        mandala_test.column_00 = data["column_00"]

        mandala_test.column_11 = data["column_11"]
        mandala_test.column_12 = data["column_12"]
        mandala_test.column_13 = data["column_13"]
        mandala_test.column_14 = data["column_14"]
        mandala_test.column_15 = data["column_15"]
        mandala_test.column_16 = data["column_16"]
        mandala_test.column_17 = data["column_17"]
        mandala_test.column_18 = data["column_18"]
        mandala_test.column_19 = data["column_19"]

        mandala_test.column_21 = data["column_21"]
        mandala_test.column_22 = data["column_22"]
        mandala_test.column_23 = data["column_23"]
        mandala_test.column_24 = data["column_24"]
        mandala_test.column_25 = data["column_25"]
        mandala_test.column_26 = data["column_26"]
        mandala_test.column_27 = data["column_27"]
        mandala_test.column_28 = data["column_28"]
        mandala_test.column_29 = data["column_29"]

        mandala_test.column_31 = data["column_31"]
        mandala_test.column_32 = data["column_32"]
        mandala_test.column_33 = data["column_33"]
        mandala_test.column_34 = data["column_34"]
        mandala_test.column_35 = data["column_35"]
        mandala_test.column_36 = data["column_36"]
        mandala_test.column_37 = data["column_37"]
        mandala_test.column_38 = data["column_38"]
        mandala_test.column_39 = data["column_39"]

        mandala_test.column_41 = data["column_41"]
        mandala_test.column_42 = data["column_42"]
        mandala_test.column_43 = data["column_43"]
        mandala_test.column_44 = data["column_44"]
        mandala_test.column_45 = data["column_45"]
        mandala_test.column_46 = data["column_46"]
        mandala_test.column_47 = data["column_47"]
        mandala_test.column_48 = data["column_48"]
        mandala_test.column_49 = data["column_49"]

        mandala_test.column_51 = data["column_51"]
        mandala_test.column_52 = data["column_52"]
        mandala_test.column_53 = data["column_53"]
        mandala_test.column_54 = data["column_54"]
        mandala_test.column_55 = data["column_55"]
        mandala_test.column_56 = data["column_56"]
        mandala_test.column_57 = data["column_57"]
        mandala_test.column_58 = data["column_58"]
        mandala_test.column_59 = data["column_59"]

        mandala_test.column_61 = data["column_61"]
        mandala_test.column_62 = data["column_62"]
        mandala_test.column_63 = data["column_63"]
        mandala_test.column_64 = data["column_64"]
        mandala_test.column_65 = data["column_65"]
        mandala_test.column_66 = data["column_66"]
        mandala_test.column_67 = data["column_67"]
        mandala_test.column_68 = data["column_68"]
        mandala_test.column_69 = data["column_69"]

        mandala_test.column_71 = data["column_71"]
        mandala_test.column_72 = data["column_72"]
        mandala_test.column_73 = data["column_73"]
        mandala_test.column_74 = data["column_74"]
        mandala_test.column_75 = data["column_75"]
        mandala_test.column_76 = data["column_76"]
        mandala_test.column_77 = data["column_77"]
        mandala_test.column_78 = data["column_78"]
        mandala_test.column_79 = data["column_79"]

        mandala_test.column_81 = data["column_81"]
        mandala_test.column_82 = data["column_82"]
        mandala_test.column_83 = data["column_83"]
        mandala_test.column_84 = data["column_84"]
        mandala_test.column_85 = data["column_85"]
        mandala_test.column_86 = data["column_86"]
        mandala_test.column_87 = data["column_87"]
        mandala_test.column_88 = data["column_88"]
        mandala_test.column_89 = data["column_89"]

        mandala_test.column_91 = data["column_91"]
        mandala_test.column_92 = data["column_92"]
        mandala_test.column_93 = data["column_93"]
        mandala_test.column_94 = data["column_94"]
        mandala_test.column_95 = data["column_95"]
        mandala_test.column_96 = data["column_96"]
        mandala_test.column_97 = data["column_97"]
        mandala_test.column_98 = data["column_98"]
        mandala_test.column_99 = data["column_99"]

        db.session.commit()

        success = {"success":"成功したよ！"}
        return jsonify(success)

if __name__ == "__main__":
    app.run(debug=True)