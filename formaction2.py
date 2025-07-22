from flask import Flask,redirect,render_template,url_for,request,session

app = Flask(__name__)
users = {"sreedhar":"1234","siddhu":"1144","navya":"lucky"}

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("welecome.html")
@app.route("/login",methods =["POST","GET"])
def login():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form['password']
        user_exit  = False
        for user in users:
            if username in user:
                user_exit = True

            if users[username] ==password:
                session['user']=username
                return redirect(url_for("home"))
            else:
                return "invalid try agian"
        if  not user_exit:
            return "invalid details try again" 
    elif "user" in session:
        return redirect(url_for("home"))

    return render_template("login.html")
@app.route("/logout",methods =["POST"])
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)