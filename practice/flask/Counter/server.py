from flask import Flask, render_template, session, redirect,request
app = Flask (__name__)
app.secret_key = "secret is the counter"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():
    session.pop("count")
    return redirect ('/')

@app.route('/add_reset', methods=["POST"])
def add_reset():
    if request.form["fix"]=="add":
        session["count"] += 1
    elif request.form["fix"]=="reset":
        session["count"] = 0
    return redirect("/")

@app.route('/user' ,methods=["post"])
def user():
    
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)