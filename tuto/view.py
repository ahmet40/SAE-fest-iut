
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
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, ''))
import models


@app.route("/")
def home():
    return render_template("portails.html")

@app.route("/login_spec")
def login_spec():
    """Cette methode va nous permettre de nous diriger vers la page 
        login pour les spectateurs.
    Returns:
        reder_template:direction vers la page
    """
    return render_template("login_spec.html")

@app.route("/login_admin")
def login_admin():
    """Cette methode va nous permettre de nous diriger vers la page 
        login pour les admin
    Returns:
        reder_template:direction vers la page
    """
    return render_template("login_admin.html")

@app.route("/create_account")
def create_account():
    """Cette methode va nous permettre de nous diriger vers la page 
        creation de compte
    Returns:
        reder_template:direction vers la page
    """
    return render_template("create_account.html")

@app.route("/liste_concerts")
def liste_concert():
    """Cette methode va nous permettre de nous diriger vers la page 
        liste de concerts
    Returns:
        reder_template:direction vers la page
    """
    return render_template("liste_concerts.html",liste_concert=models.liste_concert())

@app.route("/login_spec",methods=["GET","POST"])
def creation_compte():
    """Cette methode va nous permettre de nous rediriger vers la page 
        login
    Returns:
        redirect:redirection vers la page
    """
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    statut=models.creation_compte(username,email,password)
    if statut=="MailExiste":
        return redirect(url_for("create_account"))
    return redirect(url_for("login_spec"))

@app.route("/liste_concerts",methods=["GET","POST"])
def se_connecter():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts
    Returns:
        redirect:redirection vers la page
    """
    username=request.form.get("username")
    password=request.form.get("password")
    if not models.connecter_spectateur(username,password):
        return redirect(url_for("login_spec"))
        #redirection vers la page login si la connection de l'utilisateur n'a pas fonctionner
    return redirect(url_for("liste_concerts"))    #redirection vers la page principale du site internet