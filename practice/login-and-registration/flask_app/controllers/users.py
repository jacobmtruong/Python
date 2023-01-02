from crypt import methods
from flask_app import app
from flask import render_template, redirect, session, request,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    #del session["user_id"] #log user out everytime they go back to login page
    return render_template ("index.html")

@app.route('/register', methods = ['post'])
def register():
    #check the flash validation
    if not User.validate_user(request.form):
        return redirect('/')
    #check if email already in use
    data = {
        'email' : request.form ['email']
    }
    user_in_db = User.get_user_by_email(data)
    
    if user_in_db: 
        flash ('Email is already taken')
        return redirect('/success')
    else:
    #register user
    # create the hash
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {
            "first_name": request.form ["first_name"],
            "last_name": request.form ["last_name"],
            "email": request.form ["email"],
            # put the pw_hash into the data dictionary
            "password": pw_hash
        }
        # Call the save @classmethod on User
        user_id = User.register(data)
        session['user_id'] = user_id
        return redirect('/')


@app.route('/login', methods = ['post'])
def login():
    # see if the username provided exists in the database
    data = {
        'email' : request.form ['email']
    }
    user_in_db = User.get_user_by_email(data)
    # if user is not registered in the db
    if not user_in_db:
        flash ('Invalid Email/Password')
        return redirect ("/")
    # if we get False after checking the password (email is valid)
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ('Invalid Email/Password')
        return redirect ("/")
    # if the passwords matched, we set the user_id into session4
    session['user_id'] = user_in_db.id
    return redirect ("/success")

@app.route("/success")
def success():
    if "user_id" not in session:
        return redirect ("/")
    data = {
        "id": session ["user_id"]
    }
    user_in_db = User.get_user_by_id(data)
    return render_template ("user_page.html", user = user_in_db)

