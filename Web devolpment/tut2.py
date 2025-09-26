from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("Index.html")

@app.route("/Golu")
def Golu():
    return "Hello Golu"

app.run(debug=True)
