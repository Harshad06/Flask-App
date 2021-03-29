from flask import Blueprint, render_template

second_01 = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second_01.route("/home")
@second_01.route("/")
def home():
    return render_template("home.html")

@second_01.route("/test")
def test():
    return "<h1>test from second.py file</h1>"