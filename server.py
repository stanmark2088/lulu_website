from flask import Flask, request , redirect , render_template,url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route("/lulu",methods=["GET","POST"])
def lulu():
    return render_template("lulu.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True,
            port=5000)
