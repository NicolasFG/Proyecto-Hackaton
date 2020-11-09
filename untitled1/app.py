from flask import Flask,render_template,request,redirect
from re import split

import validacion_formulario as bot
from selenium import webdriver
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

# PATH="/home/fabrizio/chromedriver"
# driver=webdriver.Chrome(PATH)
app.config['UPLOAD_FOLDER'] = './files'

logeada=False


@app.route('/',methods=["GET","POST"])
def default():
    if request.method == 'POST':
        code = request.form['code']
        if code != '':
            codes = split('\D+', code)
            print(codes)
            global logeada
            dicc=bot.funcion(codes,logeada)
            if logeada==False:
                logeada=True;
            print(dicc)
            return render_template("result-form.html",s=codes,d=dicc)

        if 'file' not in request.files:
            return redirect(request.url)

        files=request.files.getlist("file")
        print(files)

        if len(files) == 0:
            return redirect(request.url)

        if files:
            for i in files:
                filename = secure_filename(i.filename)
                i.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("result-image.html")


    return render_template("index.html")


if __name__ == '__main__':
    print("hello")
    app.run()
