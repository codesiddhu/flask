from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/course")
def courses():
    return "<h1> welecome to the course </h1>"


@app.route("/<name>")
def name(name ):
    return f"<h1> welecome to the {name} </h1>"
@app.route("/admin")
def admin():
    return redirect("/")
@app.route("/url")
def url():
    return redirect(url_for("courses"))
 
if __name__ =="__main__":
    app.run()
