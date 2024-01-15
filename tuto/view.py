
import random
from flask import jsonify, render_template, url_for, redirect
from flask import request
from flask import request, redirect, url_for
from .app import app
from werkzeug.utils import secure_filename
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
from personne_bd import Personne_bd
from organisation_bd import Organisation_bd
ADMIN=Admin_bd(CNX)
SPECTATEUR=Spectateur_bd(CNX)
PERSONNE=Personne_bd(CNX)
ORGANISATION=Organisation_bd(CNX)

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
    return render_template("liste_concerts.html",liste_concert=models.get_concert_futurs(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),
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

@app.route("/admin-principale")
def admin_principale():
    """Cette methode va nous permettre de nous diriger vers la page 
        admin principale
    Returns:
        reder_template:direction vers la page
    """
    return render_template("adm_principale.html",adm_pricipale=True)

@app.route("/les-concerts")
def les_concerts():
    """Cette methode va nous permettre de nous diriger vers la page 
        liste de concerts
    Returns:
        reder_template:direction vers la page
    """
    return render_template("liste_concerts.html",liste_concert=models.liste_concert_proche(),le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),
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
                return redirect(url_for("home"))
    liste_adm=ADMIN.get_all_admins()
    if liste_adm:
        for adm in liste_adm:
            if username == adm.get_pseudo() and password == adm.get_mdp():
                le_adm.set_all(adm.get_id(),adm.get_pseudo(),adm.get_mdp())
                return redirect(url_for("admin_principale"))
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
    return render_template("recherche_style.html",nom=nom,le_spectateur=le_spectateur,liste_style_parent=models.liste_style_parent(),liste_style=models.get_style_by_style_parent(nom),liste_groupe=models.get_groupe_by_style_parent(nom),page_style=True)

@app.route("/deconnexion")
def deconnexion():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des concerts en nous deconnectant
    Returns:
        redirect:redirection vers la page
    """
    le_spectateur.set_all(-1,"","","")
    return redirect(url_for("home"))


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
    return redirect(url_for("home"))


@app.route("/groupe/<int:id>", methods=['GET', 'POST'])
def groupe(id):
    """Cette methode va nous permettre de nous rediriger vers la page 
        de l'information sur les groupes
    Returns:
        redirect:redirection vers la page
    """
    if request.method == 'GET':
        j=models.get_info_groupe(id)
        return render_template("groupe_infos.html", liste_style_parent=models.liste_style_parent(), groupe=j[0],concert_future=j[2],concert_passe=j[3],act_futur=j[4],act_passe=j[5], chanteur=j[1], le_spectateur=le_spectateur, groupe_infos=True,is_group_favorite=models.check_if_group_is_favorite(le_spectateur.get_id_p(), id))
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
    if le_spectateur.get_id_p()==-1:
        return redirect(url_for("login_spec"))
    return render_template("mes_groupes.html",liste_style_parent=models.liste_style_parent(),liste_groupe=models.get_favoris(le_spectateur.get_id_p()),le_spectateur=le_spectateur,page_groupe=True)


@app.route("/membre/<int:idg>/<int:idp>")
def membre(idg,idp):
    """Cette methode va nous permettre de nous rediriger vers la page 
        de l'information sur les groupes
    Returns:
        redirect:redirection vers la page
    """
    return render_template("infos_membre.html",liste_style_parent=models.liste_style_parent(),membre=models.get_infos_membre(idg,idp),le_spectateur=le_spectateur,info_membre=True)



@app.route("/chanteur")
def liste_chanteurs():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste des chanteurs
    Returns:
        redirect:redirection vers la page
    """
    return render_template("liste_chanteurs.html",liste_style_parent=models.liste_style_parent(),chanteur=models.get_all_chanteur(),le_spectateur=le_spectateur,page_groupe=True)


@app.route("/chanteur-groupe/<int:id>")
def get_infos_groupe(id):
    """Cette methode va nous permettre d'obtenir les informations d'un groupe

    Args:
        id ([int]): l'id du groupe

    Returns:
        list: la liste des informations
    """
    return render_template("liste_groupe.html",liste_style_parent=models.liste_style_parent(),liste_groupe=models.liste_groupe_by_idp(id),le_spectateur=le_spectateur,page_groupe=True)



@app.route("/mes-concerts")
def mes_concerts():
    """Cette methode va nous permettre de nous rediriger vers la page 
        liste de mes concerts
    Returns:
        redirect:redirection vers la page
    """
    if le_spectateur.get_id_p()==-1:
        return redirect(url_for("login_spec"))
    return render_template("mes_concerts.html",liste_style_parent=models.liste_style_parent(),liste_concert=models.concert_by_spec(le_spectateur.get_id_p()),le_spectateur=le_spectateur,page_liste=True)


@app.route("/infos-concert/<int:id>")
def infos_concert(id):
    """Cette methode va nous permettre de nous rediriger vers la page 
        de l'information sur les concerts
    Returns:
        redirect:redirection vers la page
    """
    liste = models.get_concert(le_spectateur.get_id_p(),id)
    return render_template("infos_concert.html",liste_style_parent=models.liste_style_parent(),concert=liste[0],liste_groupe=liste[1],le_spectateur=le_spectateur,info_concert=True,future_concert=liste[2],if_concert_acheter_by_spec=liste[3])


@app.route("/infos-concert/acheter/<int:id>")
def acheter_le_billet(id):
    """Cette methode va nous permettre d'acheter un billet

    Args:
        id ([int]): l'id du billet

    Returns:
        list: la liste des informations
    """
    if le_spectateur.get_id_p()!=-1:
        models.acheter_concert(le_spectateur.get_id_p(),id)
    return redirect(url_for("infos_concert",id=id))


@app.route("/infos-concert/annuler/<int:id>",methods=["POST"])
def annule_le_billet(id):
    """Cette methode va nous permettre d'acheter un billet

    Args:
        id ([int]): l'id du billet

    Returns:
        list: la liste des informations
    """
    if le_spectateur.get_id_p()!=-1:
        models.annuler_achat_concert(le_spectateur.get_id_p(),id)
    return redirect(url_for("infos_concert",id=id))


@app.route("/gerer-chanteur")
def gerer_chanteur():
    """Cette methode va nous permettre de gerer les chanteurs

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_chanteur.html",chanteur=models.get_all_chanteur(),gerer_concert=True)
    return redirect("login_spec")


@app.route("/supprimer/<int:id>",methods=["POST"])
def supprimer_le_chanteur(id):
    models.supprimer_chanteur(id)
    return redirect(url_for("gerer_chanteur"))


@app.route("/cree-chanteur",methods=["GET","POST"])
def cree_chanteur():
    """Cette methode va nous permettre de creer un chanteur

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("add_chanteur.html",add_chanteur=True)
    else:
        return redirect("login_spec")

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/add-chanteur",methods=["GET","POST"])
def add_chanteur():
    if request.method=="POST":
            nom=request.form.get("nom")
            prenom=request.form.get("prenom")
            email=request.form.get("email")
            image_file = request.files['image']

            # Vérifiez si un fichier a été téléchargé
            if image_file and allowed_file(image_file.filename):
                # Sécurisez le nom du fichier
                filename = secure_filename(image_file.filename)
                filename = filename+str(random.randint(0, 100000))
                # Enregistrez le fichier dans le répertoire "station/images"
                image_path = os.path.join("static/images", filename)
                image_file.save(image_path)
                print(PERSONNE.get_prochain_id_personne())

                # Maintenant, vous pouvez utiliser le nom du fichier (filename) comme information supplémentaire
                # dans votre base de données, par exemple:
                models.inserer_chanteur(PERSONNE.get_prochain_id_personne(), nom, prenom, email, filename)

    return redirect(url_for("gerer_chanteur"))


@app.route("/gerer-image")
def gerer_image():
    """Cette methode va nous permettre de gerer les images

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_image.html",image=models.get_all_image(),gerer_concert=True)
    return redirect("login_spec")

@app.route("/supprimer-image/<int:id>",methods=["POST"])
def supprimer_image(id):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image

    Returns:
        list: la liste des informations
    """
    print(id)
    models.supprimer_image(id)
    return redirect(url_for("gerer_image"))


@app.route("/gerer-groupe")
def gerer_groupe():
    """Cette methode va nous permettre de gerer les groupes

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_groupe.html",groupe=models.get_groupe_cpt(),gerer_concert=True)
    return redirect("login_spec")


@app.route("/gerer-membre/<int:id>")
def gerer_membre(id):
    """
        permet de gerer les groupes
    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_membre.html",chanteur=models.get_membre_liste(id),gerer_concert=True,grp=id)
    return redirect("login_spec")



@app.route("/supprimer-groupe/<int:id>",methods=["POST"])
def supprimer_groupe(id):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image

    Returns:
        list: la liste des informations
    """
    print(id)
    models.delete_groupe(id)
    return redirect(url_for("gerer_groupe"))



@app.route("/supprimer-membre/<int:id_g>/<int:id_p>",methods=["POST"])
def supprimer_membre(id_g,id_p):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image

    Returns:
        list: la liste des informations
    """
    print(id)
    models.delete_membre_par_personne(id_g,id_p)
    return redirect(url_for("gerer_membre",id=id_g))


@app.route("/cree-groupe")
def creer_groupe():
    """Cette methode va nous permettre de creer un groupe

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("add_groupe.html",add_chanteur=True)
    else:
        return redirect("login_spec")
    


@app.route("/nouveau_groupe",methods=["GET","POST"])
def nouveau_groupe():
    if request.method=="POST":
            print("hahahahaa")
            nom=request.form.get("nom")
            description=request.form.get("textarea")
            lien_reseau=request.form.get("lien_resaux")
            lien_video=request.form.get("lien_video")
            image_file = request.files['image']

            # Vérifiez si un fichier a été téléchargé
            if image_file and allowed_file(image_file.filename):
                filename, file_extension = os.path.splitext(secure_filename(image_file.filename))
                
                # Générez un nombre aléatoire
                random_number = str(random.randint(0, 100000))

                # Concaténez le nombre aléatoire avant l'extension du fichier
                filename = filename + random_number + file_extension

                # Enregistrez le fichier dans le répertoire "station/images"
                image_path = os.path.join("static/images", filename)
                image_file.save(image_path)

                # Maintenant, vous pouvez utiliser le nom du fichier (filename) comme information supplémentaire
                # dans votre base de données, par exemple:
                models.inserer_groupe(nom, description, lien_reseau, lien_video, filename)
    return redirect(url_for("gerer_groupe"))


@app.route("/cree-membre/<int:id>")
def cree_membre(id):
    """Cette methode va nous permettre de creer un membre

    Returns:
        list: la liste des informations
    """
    if le_adm.get_id()!=-1:
        return render_template("add_membre.html",grp=id,personne=models.get_all_personne_instrumement(id)[0],instrument=models.get_all_personne_instrumement(id)[1])
    else:
        return redirect("login_spec")
    

# Ajoutez cette route à votre application Flask
@app.route("/action-creer-membre/<int:id>", methods=["POST"])
def action_creer_membre(id):
    if request.method == "POST":
        id_personne = int(request.form.get("selectPersonne"))
        id_instrument = int(request.form.get("selectInstrument"))

        # Faites quelque chose avec les identifiants sélectionnés, par exemple, ajoutez-les à la base de données
        models.creer_membre(id,id_personne, id_instrument)

    # Redirigez ou renvoyez une réponse appropriée
    return redirect(url_for("gerer_membre",id=id))



@app.route("/gerer-concert")
def gerer_concert():
    """Cette methode va nous permettre de gerer les concerts


    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_concerts.html",liste_concert=models.get_concerts_nb_groupe_img(),gerer_concert=True)
    return redirect("login_spec")

@app.route("/cree-concert")
def creer_concert():
    """Cette methode va nous permettre de creer un groupe

    """
    if le_adm.get_id()!=-1:
        return render_template("add_concert.html",add_chanteur=True)
    else:
        return redirect("login_spec")
    

@app.route("/supprimer-concert/<int:id>",methods=["POST"])
def supprimer_concert(id):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image

    Returns:
        list: la liste des informations
    """
    models.delete_concert(id)
    return redirect(url_for("gerer_concert"))

@app.route("/gerer-groupe-concert/<int:id>")
def gerer_groupe_concert(id):
    """
        permet de gerer les groupes des concerts
    """
    if le_adm.get_id()!=-1:
        return render_template("gerer_groupe_concert.html",groupes=models.get_groupe_concert_liste(id),gerer_concert=True,concert=id)
    return redirect("login_spec")

@app.route("/ajouter-groupe-concert/<int:id>")
def ajouter_groupe(id):
    """Cette methode va nous permettre d'ajouter un groupe à un concert'

    """
    if le_adm.get_id()!=-1:
        return render_template("add_groupe_concert.html",groupes=models.liste_groupe_absent_concert(id),gerer_concert=True,concert=models.get_concert_id(id))
    else:
        return redirect("login_spec")

@app.route("/ajouter-groupe-concert/<int:id>")
def ajouter_groupe_popup(id,message,show_popup):
    """Cette methode va nous permettre d'ajouter un groupe à un concert'

    """
    if le_adm.get_id()!=-1:
        print(message, show_popup)
        return render_template("add_groupe_concert.html",groupes=models.liste_groupe_absent_concert(id),gerer_concert=True,concert=models.get_concert_id(id),msg=message,show_popup=show_popup)
    else:
        return redirect("login_spec")

@app.route("/supprimer-groupe-concert/<int:id_c>/<int:id_g>",methods=["POST"])
def supprimer_groupe_concert(id_c,id_g):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image

    Returns:
        list: la liste des informations
    """
    models.delete_groupe_concert(id_c,id_g)
    return redirect(url_for("gerer_groupe_concert",id=id_c))


@app.route("/action-ajouter-groupe-concert/<int:id_c>/<int:id_g>", methods=["POST"])
def action_ajouter_groupe_concert(id_c, id_g):
    if request.method == "POST":
        debut = str(request.form.get("debut_concert"))
        fin = str(request.form.get("fin_concert"))

        messages = models.inserer_dans_organisation(id_c, id_g, debut, fin)
        print(messages)
        return redirect(url_for("ajouter_groupe_popup",id=id_c , erreur_insertion=messages,show_popup=True))

