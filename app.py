from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root123@localhost/noticeboard"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Notice(db.Model):
    __tablename__ = "notices"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50))
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/login", methods=["POST"])  # <-- PASTE IT HERE
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    print("Got username:",username,"password:",password)
    # For now we use hardcoded admin. Later we can use database
    if username == "admin" and password == "admin123":
        return jsonify({"success": True, "message": "Login Successful"})
    else:
        return jsonify({"success": False, "message": "Invalid Credentials"}), 401
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

    @app.route("/add_notice", methods=["POST"])
    def add_notice():
     data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    new_notice = Notice(
        title=title,
        content=content
    )

    db.session.add(new_notice)
    db.session.commit()

    return jsonify({
        "message": "Notice Added Successfully"
    })
   
    with app.app_context():
       db.create_all()

if __name__ == "__main__":
    app.run(debug=True)