from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "helllo worlds"
@app.route("/helloworld")
def helloworld():
    ans =[]
    for i in range(0,10):
        ans.append(i)
    
    return ans

def about():
    return "about pages "
app.add_url_rule("/about","about",about)

#variables declaerds

def veriables(guest):
    return f"this is the variables decalrations {guest}"
app.add_url_rule("/veriables/<guest>","veriables",veriables)

#redirect method and url for 
app.route("/admin")
def admin():
    return "this is the admin pages "

def guest(guest):
    return f"this veriables {guest}"

def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest =name))
app.add_url_rule("/user/<name>","user",user)





if __name__ =="__main__":
  
    app.run(debug=True)