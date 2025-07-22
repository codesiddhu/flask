from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
users = {"siddhu":"1144"}
@app.route("/")
def home():
    return render_template("welecome.html")
@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method =="POST":
        username = request.form['username']
        password = request.form["password"]
        if users[username] ==password:
            return redirect(url_for('home'))
        else:
            return "invalid please try agian :"
        
    return render_template("login.html")
@app.route("/logout",methods = ["POST"])
def logout():
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug = True)