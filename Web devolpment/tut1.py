from flask import Flask




app = Flask(__name__)
@app.route("/")
def Hello():
    return  "Hello Word"

@app.route("/Golu")
def Golu():
    return  "Hello Golu"


app.run(debug=True)