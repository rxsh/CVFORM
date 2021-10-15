from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/form-cv", methods=["POST"])
def cv():
    name = request.form.get("name")
    return render_template("index.html")
