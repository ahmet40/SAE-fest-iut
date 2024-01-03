
from flask import jsonify, render_template, url_for, redirect
from flask import request
from flask import request, redirect, url_for
from .app import app
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, ''))
import models
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './modele')
sys.path.append(os.path.join(ROOT, './bd'))
from connexion import CNX
from spectateur_bd import Spectateur_bd
from admin_bd import Admin_bd
ADMIN=Admin_bd(CNX)
SPECTATEUR=Spectateur_bd(CNX)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './modele')
sys.path.append(os.path.join(ROOT, './code_modele'))
from spectateur import Spectateur
from admin import Admin

le_spectateur=Spectateur(-1,"","","")
le_adm=Admin(-1,"","")

@app.route("/")
def home():
    """
    Cette methode va nous permettre de nous diriger vers la page d'accueil
    """
    print(models.liste_concert())
    return render_template("liste_concerts.html",liste_concert=models.liste_concert(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),
                           liste_concert_proche=models.liste_concert_proche(),page_liste=True)

@app.route("/login_spec")
def login_spec():
    """Cette methode va nous permettre de nous diriger vers la page 
        login pour les spectateurs.
    Returns:
        reder_template:direction vers la page
    """
    return render_template("login_spec.html")

@app.route("/create_account")
def create_account():
    """Cette methode va nous permettre de nous diriger vers la page 
        creation de compte
    Returns:
        reder_template:direction vers la page
    """
    return render_template("create_account.html")



@app.route("/les-concerts")
def les_concerts():
    """Cette methode va nous permettre de nous diriger vers la page 
        liste de concerts
    Returns:
        reder_template:direction vers la page
    """
    return render_template("liste_concerts.html",liste_concert=models.liste_concert(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),
                           liste_concert_proche=models.liste_concert_proche(),page_liste=True)

@app.route("/inscription",methods=["GET", "POST"])
def inscrire():
    """Cette methode va nous permettre de nous rediriger vers la page 
        login
    Returns:
        redirect:redirection vers la page
    """
    if request.method == "POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        print(username,email,password)
        liste_utilisateur=SPECTATEUR.get_all_spectateurs()
        for utilisateur in liste_utilisateur:
            if email==utilisateur.get_email() or username==utilisateur.get_pseudo():
                return jsonify({"error": "exists"})
        models.inserer_le_spectateur(username, email, password)
        le_spectateur.set_all(SPECTATEUR.get_prochain_id_spectateur() - 1,
                                username, email, password)
        return jsonify({"success": "registered"})
    return redirect(url_for("create_account"))

@app.route("/les-concerts",methods=["GET", "POST"])
def connecter():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts
    Returns:
        redirect:redirection vers la page
    """
    username=request.form.get("username")
    password=request.form.get("password")
    print(username,password)
    liste_spec = SPECTATEUR.get_all_spectateurs()
    if liste_spec:
        for spec in liste_spec:
            if (username == spec.get_pseudo() or username == spec.get_email()) and password == spec.get_mdp():
                le_spectateur.set_all(spec.get_id_p(),spec.get_pseudo(),spec.get_email(),spec.get_mdp())
                return redirect(url_for("les_concerts"))
    liste_adm=ADMIN.get_all_admins()
    if liste_adm:
        for adm in liste_adm:
            if username == adm.get_pseudo() and password == adm.get_mdp():
                return render_template("login_admin.html")
    
    return redirect(url_for("login_spec"))

@app.route("/les-regions")
def recherche_region():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts
    Returns:
        redirect:redirection vers la page
    """
    return render_template("recherche_region.html",le_spectateur=le_spectateur,page_carte=True,liste_style_parent=models.liste_style_parent())

@app.route("/les-regions/<string:nom>")
def recherche_region_nom(nom):
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts
    Returns:
        redirect:redirection vers la page
    """
    return render_template("resultat_recherche_region.html",le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),nom=nom,liste_c=models.get_concert_par_region(nom),page_liste=True)


@app.route("/recherche-style/<string:nom>")
def recherche_style(nom):
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts
    Returns:
        redirect:redirection vers la page
    """
    print(models.get_groupe_by_style_parent(nom))
    return render_template("recherche_style.html",nom=nom,le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),liste_style=models.get_style_by_style_parent(nom),liste_grp=models.get_groupe_by_style_parent(nom),page_style=True)

@app.route("/deconnexion")
def deconnexion():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts en nous deconnectant
    Returns:
        redirect:redirection vers la page
    """
    le_spectateur.set_all(-1,"","","")
    return redirect(url_for("les_concerts"))


@app.route("/groupes")
def groupes():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des groupes
    Returns:
        redirect:redirection vers la page
    """
    return render_template("liste_groupe.html",liste_style=models.liste_style(),liste_groupe=models.get_all_groupe(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),page_groupe=True)


@app.route("/groupes/<string:nom>")
def groupe_par_style(nom):
    """Cette methode va nous permettre de nous rediriger vers la page 
        groupes par style
    Returns:
        redirect:redirection vers la page
    """
    return render_template("resultat_recherche_groupe.html",nom=nom,liste_groupe=models.get_groupe_par_style(nom),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),page_groupe=True)

@app.route("/passé")
def concert_passer():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts passés
    Returns:
        redirect:redirection vers la page
    """
    return render_template("a_venir_passe.html",liste_concert=models.get_concert_finis(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),page_liste=True)

@app.route("/futurs")
def concert_futurs():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts futurs
    Returns:
        redirect:redirection vers la page
    """
    return render_template("a_venir_passe.html",liste_concert=models.get_concert_futurs(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),page_liste=True)



@app.route("/groupe/<int:id>", methods=['GET', 'POST'])
def groupe(id):
    """Cette methode va nous permettre de nous rediriger vers la page 
        de l'information sur les groupes
    Returns:
        redirect:redirection vers la page
    """
    if request.method == 'GET':
        return render_template("groupe_infos.html", liste_style_parent=models.liste_style_parent(), groupe=models.get_info_groupe(id)[0], membre=models.get_info_groupe(id)[1], le_spectateur=le_spectateur, groupe_infos=True,is_group_favorite=models.check_if_group_is_favorite(le_spectateur.get_id_p(), id))
    # Assuming you have a function to check if the group is already in favorites
    while request.method == 'POST':
        user_id = le_spectateur.get_id_p()
        group_id = id
        is_checked = request.json.get('isChecked')
        print(f"User ID: {user_id}, Group ID: {group_id}, Is Checked: {is_checked}")
        if is_checked:
            # Add the group to favorites
            print("bonjour")
            models.add_group_to_favorites(le_spectateur.get_id_p(), id)
            return jsonify({'status': 'added'})
        else:
            print("au revoir")
            # Remove the group from favorites
            models.remove_group_from_favorites(le_spectateur.get_id_p(), id)
            return jsonify({'status': 'removed'})
            

@app.route("/mes-groupes")
def mes_groupes():
    """Cette methode va nous permettre de nous rediriger vers la page 
        groupes favoris
    Returns:
        redirect:redirection vers la page
    """
    return render_template("mes_groupes.html",liste_style_parent=models.liste_style_parent(),liste_groupe=models.get_favoris(le_spectateur.get_id_p()),le_spectateur=le_spectateur,page_groupe=True)


@app.route("/membre/<int:idg>/<int:idp>")
def membre(idg,idp):
    """Cette methode va nous permettre de nous rediriger vers la page 
        de l'information sur les groupes
    Returns:
        redirect:redirection vers la page
    """
    return render_template("infos_membre.html",liste_style_parent=models.liste_style_parent(),membre=models.get_infos_membre(idg,idp),le_spectateur=le_spectateur,info_membre=True)

