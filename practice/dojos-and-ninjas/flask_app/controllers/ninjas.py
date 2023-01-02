from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("home.html", all_dojos=all_dojos)


@app.route("/dojos")
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=all_dojos)



@app.route("/submit", methods=["post"])
def add_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojos_id": request.form["dojos_id"]
    }
    Ninja.save(data)
    return redirect ("/dojos")


@app.route("/add_dojo", methods = ["post"])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.add_dojo(data)
    return redirect ("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.find_one(data)
    return render_template ("dojo_show.html", dojo = dojo)

