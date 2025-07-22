from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/user")
def user():
    data ={"username":"siddhu royals "}
    return render_template("hello.html",data=data)

if __name__=="__main__":
    app.run(debug=True)