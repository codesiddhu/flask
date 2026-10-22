
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["user_name"]
        return redirect(url_for("user_f", user_name=user))

    return render_template("home.html")


@app.route("/<user_name>")
def user_f(user_name):
    return f"Welcome to {user_name}"


if __name__ == "__main__":
    app.run(debug=True)
