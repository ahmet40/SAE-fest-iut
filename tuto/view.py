
from flask import jsonify, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from flask import request
from hashlib import sha256
from wtforms import PasswordField
from flask import request, redirect, url_for
from wtforms import FloatField
from flask import flash
from .app import app, db
import sqlalchemy
import os
import sys


@app.route("/")
def home():
    return render_template("portails.html")

@app.route("/login_spec")
def login_spec():
    return render_template("login_spec.html")

@app.route("/login_admin")
def login_admin():
    return render_template("login_admin.html")

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")