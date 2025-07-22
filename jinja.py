from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    data = [
        {"name":"siddhu",
         "id":101,
         "locaton":"tadipatri"
        },
        {
            "name":"sreedhar",
            "id":102,
            "location":"tirupati"
        }
    ]
    return render_template("jinjaHome.html",data = data)


if __name__ == "__main__":
    app.run(debug =True)