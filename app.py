from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("login.html")
db={'admin':'123','user':'123','cv':'123'}

@app.route('/form_cv',methods=['POST','GET'])
def login():
    usr=request.form['username']
    pwd=request.form['password']
    if usr not in db:
	    return render_template('login.html',info='Invalid User')
    else:
        if db[usr]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=usr)

@app.route('/my_cv', methods=['POST','GET'])
def datos():
    nombre = request.form.GET("fnombre")
    job = request.form.GET("fjob")
    age = request.form.GET("fage")
    email = request.form.GET("femail")
    phone = request.form.GET("fcelular")
    address = request.form.GET("fnacionalidad")
    resumen = request.form.GET("fresumen")
    exp_laboral = request.form.GET("fexp-laboral")
    educacion = request.form.GET("primaria")
    logros = request.form.GET("flogros")
    habilidades = request.form.GET("fhabilidades")
    references = request.form.GET("freferencias")
    intereses = request.form.GET("fintereses")

    return render_template('cv3.html', nombre=nombre, job=job, age=age, email=email, phone=phone,
    address=address, resumen=resumen, exp_laboral=exp_laboral, educacion=educacion,
    logros=logros, habilidades=habilidades, references=references, intereses=intereses)

if __name__ == '__main__':
    app.run()
