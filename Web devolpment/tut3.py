from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Index.html")

@app.route("/bootstrap")
def about():
    return render_template("about.html")
@app.route("/bootstrap")
def contact():
    return render_template("contact.html")


app.run(debug=True)