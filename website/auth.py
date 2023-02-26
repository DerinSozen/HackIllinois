from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth",__name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login Success!")
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Credentials")
        else:
            flash("Could Not Find Email In Records")
    return render_template("login.html",)

@auth.route("/logout")
@login_required
def logout():
    logout_user
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email is already taken")
        elif len(email) < 4:
            flash("Email must be at least 4 characters")
        elif len(first_name) < 2:
            flash("Name must be at least 2 characters")
        elif len(password) < 7:
            flash("Password must be at least 7 characters")
        else:
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password,method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash("Account Creation Successful")
            return redirect(url_for("views.home"))
        
    return render_template("sign_up.html")