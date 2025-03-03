from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("templates/index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("templates/resume_1.html")

@app.route('/resume_template')
def resume_template():
    return render_template("templates/resume_template.html")

if(__name__ == "__main__"):
    app.run()
