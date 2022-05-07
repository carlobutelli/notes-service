#!/usr/bin/env python3
from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route('/')
def home_view():
    return render_template("home.html")
