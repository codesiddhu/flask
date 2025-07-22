from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def about():
    return "wleome app"

def guest(guest):
   
    return f"this is {guest}"
app.add_url_rule("/guest/<guest>","guest",guest)

@app.route("/user_name/<string:name>")
def user_name(name):
    return f"this is username dispalyes here {name}"
@app.route("/user_id/<int:id>")
def user_id(id):
    return f"this is user id {id}"



if __name__ =="__main__":
    app.run(debug=True)