from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def inicio():
    session.pop("usr", None)
    return render_template("login.html")

db={'admin':'123','user':'123','cv':'123'}
@app.route("/form_cv",methods=['POST','GET'])
def login():
    usr=request.form.get('username')
    pwd=request.form.get('password')
    session["usr"] = usr

    if usr not in db:
	    return render_template('login.html',info='Invalid User')
    else:
        if db[usr]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('templates.html',name=usr)

@app.route("/choose", methods=['POST','GET'])
def choose():
    cvs = request.form.get('CV')
    session['cvs'] = cvs

    if "usr" not in session:
        return render_template('login.html')
    else:
        usr = session["usr"]
        return render_template('index.html')

@app.route("/my_cv", methods=["GET","POST"])
def datos():
    nombre = request.form.get("fnombre")
    job = request.form.get("fjob")
    age = request.form.get("fage")
    email = request.form.get("femail")
    phone = request.form.get("fcelular")
    address = request.form.get("fnacionalidad")
    resumen = request.form.get("fresumen")
    exp_laboral = request.form.get("fexp-laboral")
    educacion = request.form.get("feducacion")
    logros = request.form.get("flogros")
    habilidades = request.form.get("fhabilidades")
    references = request.form.get("freferencias")
    intereses = request.form.get("fintereses")
    cvs = session["cvs"]

    return render_template("Cvs.html",nombre=nombre,job=job,age=age,email=email,phone=phone,
    address=address,resumen=resumen,exp_laboral=exp_laboral,educacion=educacion,logros=logros,
    habilidades=habilidades,references=references,intereses=intereses,cvs=cvs)

if __name__ == '__main__':
    app.run()