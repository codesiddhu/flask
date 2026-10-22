from flask import Flask,redirect,render_template,url_for,session,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def login_page():
    if request.method =="POST":
        user = request.form["user_name"]
        session['users'] = user
        return redirect(url_for("user_login"))

    return render_template("login.html")
@app.route("/index")
def index_page():
    return render_template("index.html") 
@app.route("/user")
def user_login():
    if 'users' in session:
        user =session['users']
        return f"welecome to the {user}"

if __name__ =="__main__":
    app.run(debug=True)
