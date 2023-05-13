from django.shortcuts import render
from .models import Metiers
from django.shortcuts import render, redirect, get_object_or_404
from .models import Utilisateurs, Profils, Statuts, Etudiants
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from .models import Secteurs, Metiers, Domaines, Entreprises, Diplomes,OffreStage, Candidatures
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.db import models
from datetime import datetime
from django.contrib.auth import logout
# Active la gestion des sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def accueil(request):
    erreur = None
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        # recupérer utilisateur avec le email et le password
        utilisateur = Utilisateurs.objects.filter(email=login,password=password).first()
        if utilisateur:
            id_user = utilisateur.id_user
            request.session['id_user'] = id_user
            profil=utilisateur.id_profil
            lib_profil=profil.lib_profil
            statut=utilisateur.id_statut
            lib_statut=statut.lib_statut
            if lib_statut =='D':
                erreur="Votre compte est désactivé, Veuillez contacter l'administrateur!"
                return render(request, 'accueil.html', {'erreur': erreur})
            if lib_profil == 'Etudiant':
                return redirect('etu_chercher_stage') # Remplacez 'accueil_etudiant' par le nom de la vue pour la page d'accueil des étudiants
            elif lib_profil == 'Administrateur':
                return redirect('admin_creer_util') # Remplacez 'accueil_admin' par le nom de la vue pour la page d'accueil des administrateurs
            elif lib_profil == 'Entreprise':
               return redirect('ent_publier_offre') # Remplacez 'accueil_entreprise' par le nom de la vue pour la page d'accueil des entreprises
        else:
                # Gérer le cas où les informations de connexion sont incorrectes
            erreur ="Login ou password incorrects"
           
    return render(request, 'accueil.html', {'erreur': erreur})


def ent_publier_offre(request):
    domaines = Domaines.objects.all()
    secteurs = Secteurs.objects.all()
    metiers = Metiers.objects.none()
    diplomes = Diplomes.objects.all()
    id_user = request.session.get('id_user', None)
    if request.method == 'GET':
        id_dom = request.GET.get('domaine')
        id_sec = request.GET.get('secteur')
        id_metier = request.GET.get('metier')
        # Stocker les valeurs dans la session
        if id_dom:
            request.session['id_dom'] = id_dom
        if id_sec:
            request.session['id_sec'] = id_sec
        if id_metier:
            request.session['id_metier'] = id_metier

        # Récupérer les valeurs stockées dans la session
        stored_id_dom = request.session.get('id_dom')
        stored_id_sec = request.session.get('id_sec')
        stored_id_metier = request.session.get('id_metier')

        if stored_id_dom:
            secteurs = secteurs.filter(id_dom=stored_id_dom)
        if stored_id_sec:
            metiers = Metiers.objects.filter(id_sec=stored_id_sec)
  
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        nom = utilisateur.nom
        code_postal = utilisateur.code_postal
        commune = utilisateur.commune

        if Entreprises.objects.filter(id_user=id_user).exists():
            entreprise = get_object_or_404(Entreprises, id_user=id_user)
            desc_ent = entreprise.desc_ent
            id_ent = entreprise.id_ent
        else:
            desc_ent = ""
        context = {
            'domaines': domaines,
            'secteurs': secteurs,
            'metiers': metiers,
            'id_dom' : id_dom,
            'id_sec' : id_sec,
            'id_metier' : id_metier,
            'desc_ent': desc_ent,
            'id_ent' : id_ent,
            'id_user': id_user,
            'nom': nom,
            'code_postal': code_postal,
            'commune':commune,
            'diplomes' : diplomes
         } 
        return render(request, 'ent_publier_offre.html', context)
  
    if request.method == 'POST':
        # Récupérer les valeurs stockées dans la session
        id_dom = request.session.get('id_dom')
        print("id_dom= ",id_dom)
        id_sec = request.session.get('id_sec')
        print("id_sec= ",id_sec)
        id_metier = request.session.get('id_metier')
        print("id_metier= ",id_metier)
        id_user = request.POST.get('id_user')
        print("id_user= ",id_user)
       # id_dom = request.POST.get('domaine')
        #print("id_dom= ",id_dom)
        #id_sec = request.POST.get('secteur')
        #print("id_sec= ",id_sec)
        #id_metier = request.POST.get('metier')
       # print("id_metier= ",id_metier)
        titre = request.POST.get('titre')
        print("titre= ",titre)
        id_ent = request.POST.get('id_ent')
        print("id_ent= ",id_ent)
        nom = request.POST.get('nom')
        print("nom= ",nom)
        code_postal = request.POST.get('code_postal')
        print("code_postal= ",code_postal)
        desc_ent = request.POST.get('desc_ent')
        print("desc_ent= ",desc_ent)
        commune = request.POST.get('commune')
        print("commune= ",commune)
        description = request.POST.get('description')
        print("description= ",description)
        id_dipl = request.POST.get('diplome')
        print("id_dipl= ",id_dipl)
        date_debut = request.POST.get('date_debut')
        print("date_debut= ",date_debut)
        duree = request.POST.get('duree')
        print("duree= ",duree)
        #date de publication est la date du jour
        print("date de publication= ",datetime.now())
        # pas de get sur les champs readonly nom, code_postal, commune, desc_ent
        if not id_dom or not id_sec or not id_metier or not titre or not description or not id_dipl or not date_debut or not duree:
            erreur ="Veuillez remplir tous les champs saisissables"
            print("erreur= ",erreur)
            context = {
                'id_user': id_user,
                'domaine' : id_dom,
                'secteur': id_sec,
                'metier': id_metier,
                'titre': titre,
                'nom': nom,
                'code_postal': code_postal,
                'commune': commune,
                'desc_ent': desc_ent,
                'description':description,
                'date_debut': date_debut,
                'duree': duree,
                'diplome' : id_dipl,
                'domaines' : Domaines.objects.all(),
                'secteurs' : Secteurs.objects.filter(id_dom=id_dom),
                'metiers' : Metiers.objects.filter(id_sec=id_sec),
                'diplomes' : Diplomes.objects.all(),
                'erreur' : erreur
            }
            return render(request, 'ent_publier_offre.html', context)
    
        # mise en base de l'offre de stage avec le statut EA-En attente
        statut_attente = Statuts.objects.get(lib_statut='EA')
        domaine=Domaines.objects.get(id_dom=id_dom)
        secteur=Secteurs.objects.get(id_sec=id_sec)
        metier=Metiers.objects.get(id_metier=id_metier)
        entreprise=Entreprises.objects.get(id_ent=id_ent)
        diplome=Diplomes.objects.get(id_dipl=id_dipl)
        offre_stage = OffreStage(id_dom=domaine, id_sec=secteur, id_metier=metier, desc_stage=description, duree=duree, date_debut=date_debut, date_pub=datetime.now(), id_ent=entreprise,localisation=commune,id_dipl=diplome,titre_offre=titre, id_statut=statut_attente)
        offre_stage.save()
        messages.success(request,"L\'offre de stage a été insérée avec succès!")
        return redirect('ent_publier_offre')
    return render(request, 'ent_publier_offre.html')
    

    
def ent_consult_cand(request):
    return render(request, 'ent_consult_cand.html')

def ent_mon_profil(request):
    id_user = request.session.get('id_user', None)
    if request.method == 'GET':
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        nom = utilisateur.nom
        email = utilisateur.email
        num_tel = utilisateur.num_tel
        num_voie = utilisateur.num_voie
        nom_voie = utilisateur.nom_voie
        code_postal = utilisateur.code_postal
        commune = utilisateur.commune

        if Entreprises.objects.filter(id_user=id_user).exists():
            entreprise = get_object_or_404(Entreprises, id_user=id_user)
            desc_ent = entreprise.desc_ent
        else:
            desc_ent = ""
        context = {
            'desc_ent': desc_ent,
            'id_user': id_user,
            'nom': nom,
            'email': email,
            'num_tel': num_tel,
            'num_voie': num_voie,
            'nom_voie': nom_voie,
            'code_postal': code_postal,
            'commune':commune
        } 

    if request.method == 'POST':
        desc_ent = request.POST.get('desc_ent')
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        nom = utilisateur.nom
        email = utilisateur.email
        num_tel = utilisateur.num_tel
        num_voie = utilisateur.num_voie
        nom_voie = utilisateur.nom_voie
        code_postal = utilisateur.code_postal
        commune = utilisateur.commune
        if not desc_ent:
            erreur ="le champ Description est obligatoire!"
            context = {
                'nom' : nom,
                'email' : email,
                'num_tel' : num_tel,
                'num_voie' : num_voie,
                'nom_voie' : nom_voie,
                'code_postal' : code_postal,
                'commune' : commune,
                'desc_ent': desc_ent,
                'id_user': id_user,
                'erreur' : erreur
            }
            return render(request, 'ent_mon_profil.html', context)
        else:
            # update or insert a row in the entreprises table
            print("id_user= ",id_user)
            print("desc_ent= ",desc_ent)
            if Entreprises.objects.filter(id_user=id_user).exists():
                #maj desc_ent dans entreprises
                entreprise = Entreprises.objects.get(id_user=id_user)
                entreprise.desc_ent=desc_ent
                entreprise.save()
                messages.success(request, 'La description a été modifiée avec succès.')
                return redirect('ent_publier_offre')
            else:
                # insertion de desc_ent dans la table entreprises
                utilisateur=Utilisateurs.objects.get(id_user=id_user)
                entreprise = Entreprises(id_user=utilisateur, desc_ent=desc_ent)
                entreprise.save()
                messages.success(request, 'La description a été insérée avec succès.')
                return redirect('ent_publier_offre')
    
    return render(request, 'ent_mon_profil.html', context)




    

def etu_chercher_stage(request):
    domaines = Domaines.objects.all()
    secteurs = Secteurs.objects.all()
    metiers = Metiers.objects.none()
    if request.method == 'GET':
        id_dom = request.GET.get('domaine')
        id_sec = request.GET.get('secteur')
        id_metier = request.GET.get('metier')

        # Stocker les valeurs dans la session
        if id_dom:
            request.session['id_dom'] = id_dom
        if id_sec:
            request.session['id_sec'] = id_sec
        if id_metier:
            request.session['id_metier'] = id_metier

        # Récupérer les valeurs stockées dans la session
        stored_id_dom = request.session.get('id_dom')
        stored_id_sec = request.session.get('id_sec')
        stored_id_metier = request.session.get('id_metier')

        if stored_id_dom:
            secteurs = secteurs.filter(id_dom=stored_id_dom)
        if stored_id_sec:
            metiers = Metiers.objects.filter(id_sec=stored_id_sec)
        context = {
            'domaines': domaines,
            'secteurs': secteurs,
            'metiers': metiers,
            'id_dom' : id_dom,
            'id_sec' : id_sec,
            'id_metier' : id_metier
         } 
    
        return render(request, 'etu_chercher_stage.html', context)
    if request.method == 'POST':
        erreur=""
        print("request_method=",request.method)
        # Récupérer les valeurs stockées dans la session
        id_dom = request.session.get('id_dom')
        print("id_dom= ",id_dom)
        id_sec = request.session.get('id_sec')
        print("id_sec= ",id_sec)
        id_metier = request.session.get('id_metier')
        print("id_metier= ",id_metier)
       
        if not id_dom or not id_sec or not id_metier :
            erreur ="Les 3 critères de recherche doivent être renseignés!"
            print("erreur= ",erreur)
            context = {
                'domaine' : id_dom,
                'secteur': id_sec,
                'metier': id_metier,
                'domaines' : Domaines.objects.all(),
                'secteurs' : Secteurs.objects.filter(id_dom=id_dom),
                'metiers' : Metiers.objects.filter(id_sec=id_sec),
                'erreur' : erreur
            }
            return render(request, 'etu_chercher_stage.html', context)
    
        # recherche des offres de stage avec le statut P-Publié
        statut_publie= Statuts.objects.get(lib_statut='P')
        #domaine=Domaines.objects.get(id_dom=id_dom)
        #secteur=Secteurs.objects.get(id_sec=id_sec)
        #metier=Metiers.objects.get(id_metier=id_metier)
        offres_filtrees = OffreStage.objects.filter(id_dom=id_dom, id_sec=id_sec, id_metier=id_metier, id_statut=statut_publie)
        if not offres_filtrees:
            erreur="Aucune offre de stage correspondant aux critères!"
            context = {
                'domaine' : id_dom,
                'secteur': id_sec,
                'metier': id_metier,
                'domaines' : Domaines.objects.all(),
                'secteurs' : Secteurs.objects.filter(id_dom=id_dom),
                'metiers' : Metiers.objects.filter(id_sec=id_sec),
                'offres_filtrees':offres_filtrees,
                'erreur' : erreur
            }
            return render(request, 'etu_chercher_stage.html', context)

        for offre in offres_filtrees:
            offres_stage = offres_filtrees.select_related('id_ent', 'id_ent__id_user')
            offres_diplome = offres_filtrees.select_related('id_dipl', 'id_dipl__id_dipl')
            lib_diplomes = {offre.id_dipl.lib_dipl for offre in offres_stage}
            noms_utilisateurs = {offre.id_ent.id_user.nom for offre in offres_stage}
            email_utilisateurs = {offre.id_ent.id_user.email for offre in offres_stage}
            desc_entreprises = {offre.id_ent.desc_ent for offre in offres_stage}
        # préparation du id_user_etudiant, id_user_entreprise
        id_user_etu = request.session.get('id_user', None)
        context = {
                'domaine' : id_dom,
                'secteur': id_sec,
                'metier': id_metier,
                'domaines' : Domaines.objects.all(),
                'secteurs' : Secteurs.objects.filter(id_dom=id_dom),
                'metiers' : Metiers.objects.filter(id_sec=id_sec),
                'offres_filtrees':offres_filtrees,
                'offres_stage' : offres_stage,
                'noms_utilisateurs': noms_utilisateurs ,
                'email_utilisateurs': email_utilisateurs ,
                'desc_entreprises': desc_entreprises ,
                'offres_diplome' : offres_diplome,
                'lib_diplomes' : lib_diplomes,
                'id_user_etu' : id_user_etu,
                'erreur' : erreur
            }
        return render(request, 'etu_chercher_stage.html', context)
    return render(request, 'etu_chercher_stage.html')

def etu_postuler_stage(request):
    if request.method == 'GET':
        id_user_etu = request.GET.get('id_user_etu')
        id_offre = request.GET.get('id_offre')
        print("id_offre= ",id_offre)
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user_etu)
        cv_et_lm_inexistant =0
        cv_ou_lm_inexistant =0
        if Etudiants.objects.filter(id_user=id_user_etu).exists():
             etudiant = Etudiants.objects.get(id_user=id_user_etu)
             id_user_etu = etudiant.id_etu
             if etudiant.cv is None and etudiant.lm is None:
                 print("les 2 champs sont nuls")
                 cv_et_lm_inexistant =1
                 print("cv_et_lm_inexistant= ",cv_et_lm_inexistant)
                 print("cv_ou_lm_inexistant= ",cv_ou_lm_inexistant)
                  # Fermer la fenêtre popup et rafraîchir la page parente
                 response = '<script>window.close(); window.opener.location.reload();</script>'
                 return HttpResponse(response)
             elif etudiant.cv is None or etudiant.lm is None:
                  print("au moins un des champs est nul nul")
                  cv_ou_lm_inexistant =1
                  print("cv_et_lm_inexistant= ",cv_et_lm_inexistant)
                  print("cv_ou_lm_inexistant= ",cv_ou_lm_inexistant)
                 
        else:
            id_user_etu = ""
        desc_ent = request.GET.get('desc_ent')
        email = request.GET.get('email')
        nom_ent = request.GET.get('nom_ent')
        titre_offre = request.GET.get('titre_offre')
        localisation = request.GET.get('localisation')
        desc_stage = request.GET.get('description')
        date_pub = request.GET.get('date_pub')
        duree = request.GET.get('duree')
        date_debut = request.GET.get('date_debut')

        context = {
        'id_user_etu' : id_user_etu,
        'cv_et_lm_inexistant' :cv_et_lm_inexistant,
        'cv_ou_lm_inexistant' :cv_ou_lm_inexistant,
        'desc_ent' : desc_ent,
        'email' : email,
        'nom_ent' : nom_ent,
        'titre_offre' : titre_offre,
        'localisation' : localisation,
        'description' : desc_stage,
        'date_pub' : date_pub,
        'duree' : duree,
        'date_debut' : date_debut,
        'id_offre' : id_offre
         }
        return render(request, 'etu_postuler_stage.html', context)    
    if request.method == 'POST':
        id_offre = request.POST.get('id_offre')
        id_offre = OffreStage.objects.get(id_offre=id_offre)
        id_user_etu = request.POST.get('id_etu')
        id_user_etu = Etudiants.objects.get(id_etu=id_user_etu)
        print("id_user_etu= ",id_user_etu)
        id_statut = Statuts.objects.get(lib_statut='EA')
        candidature = Candidatures(id_offre=id_offre,date_cand=datetime.now(),id_etu=id_user_etu,id_statut=id_statut)
        candidature.save()
        # Ajouter un message de confirmation
        messages.success(request, 'Candidature postulée avec succès.')
        # Fermer la fenêtre popup et rafraîchir la page parente
        response = '<script>window.close(); window.opener.location.reload();</script>'
        return HttpResponse(response)
        
    
    return render(request, 'etu_chercher_stage.html', context) 

def download_cv(request, etudiant_id):
    etudiant = Etudiants.objects.get(id_etu=etudiant_id)
    cv = etudiant.cv
    response = HttpResponse(cv, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % "nom" + '_cv.pdf'
    return response

def download_lm(request, etudiant_id):
    etudiant = Etudiants.objects.get(id_etu=etudiant_id)
    lm = etudiant.lm
    response = HttpResponse(lm, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % "nom" + '_lm.pdf'
    return response

def etu_mon_profil(request):
    id_user = request.session.get('id_user', None)
    if request.method == 'GET':
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        if Etudiants.objects.filter(id_user=id_user).exists():
            etudiant = Etudiants.objects.get(id_user=id_user)
            id_etu = etudiant.id_etu
        else:
            id_etu = ""
        nom = utilisateur.nom
        prenom = utilisateur.prenom
        num_voie = utilisateur.num_voie
        nom_voie = utilisateur.nom_voie
        commune = utilisateur.commune
        code_postal = utilisateur.code_postal
        context = {
            'id_user': id_user,
            'nom' : nom,
            'prenom': prenom,
            'num_voie': num_voie,
            'nom_voie': nom_voie,
            'commune':commune,
            'code_postal': code_postal,
            'id_etu' : id_etu
        } 
    if request.method == 'POST':
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        nom = utilisateur.nom
        prenom = utilisateur.prenom
        num_voie = utilisateur.num_voie
        nom_voie = utilisateur.nom_voie
        code_postal = utilisateur.code_postal
        commune = utilisateur.commune
        # aucun fichier n'est présent pour l'upload
        if ('cv' not in request.FILES and 'lm' not in request.FILES):
            erreur ="Aucun document à mettre à jour!"
            context = {
                'id_user': id_user,
                'nom' : nom,
                'prenom': prenom,
                'num_voie': num_voie,
                'nom_voie': nom_voie,
                'commune':commune,
                'code_postal': code_postal,
                'erreur' : erreur
            }
            return render(request, 'etu_mon_profil.html', context)
        else:
            # tester si utilisateur existe dans table etudiants
            # auquel cas ce sera une maj
            if Etudiants.objects.filter(id_user=id_user).exists():
                etudiant = Etudiants.objects.get(id_user=id_user)
                if ('cv' in request.FILES and 'lm'  in request.FILES):
                    cv = request.FILES['cv'].read()
                    lm = request.FILES['lm'].read()
                    etudiant.cv = cv
                    etudiant.lm = lm
                    etudiant.save()
                    messages.success(request, 'Les 2 documents ont été modifiés avec succès!')
                    return redirect('etu_chercher_stage')
                if ('cv' in request.FILES and 'lm'  not in request.FILES):
                    cv = request.FILES['cv'].read()
                    etudiant.cv = cv
                    etudiant.save()
                    messages.success(request, 'Le CV a été modifié avec succès!')
                    return redirect('etu_chercher_stage')
                if ('cv' not in request.FILES and 'lm'  in request.FILES):
                    lm = request.FILES['lm'].read()
                    etudiant.lm = lm
                    etudiant.save()
                    messages.success(request, 'La LM a été modifiée avec succès!')
                    return redirect('etu_chercher_stage')
            else:
                # l'utilisateur n'existe pas dans la table etudiants
                # ce sera donc une insertion
                utilisateur=Utilisateurs.objects.get(id_user=id_user)
                if ('cv' in request.FILES and 'lm'  in request.FILES):
                    cv = request.FILES['cv'].read()
                    lm = request.FILES['lm'].read()
                    etudiant = Etudiants(id_user=utilisateur,cv=cv,lm=lm)
                    etudiant.save()
                    messages.success(request, 'Les 2 documents ont été insérés avec succès!')
                    return redirect('etu_chercher_stage')
                if ('cv' in request.FILES and 'lm'  not in request.FILES):
                    cv = request.FILES['cv'].read()
                    etudiant = Etudiants(id_user=utilisateur,cv=cv)
                    etudiant.save()
                    messages.success(request, 'Le CV a été inséré avec succès!')
                    return redirect('etu_chercher_stage')
                if ('cv' not in request.FILES and 'lm'  in request.FILES):
                    lm = request.FILES['lm'].read()
                    etudiant = Etudiants(id_user=utilisateur,lm=lm)
                    etudiant.save()
                    messages.success(request, 'La LM a été insérée avec succès!')
                    return redirect('etu_chercher_stage')
                
    return render(request, 'etu_mon_profil.html',context)

def telecharger_etu_cv(request,document_id):
                      
    # Récupérer le document à partir de l'identifiant
    etudiant = get_object_or_404(Etudiants, cv=document_id)
    
    # Récupérer le contenu du fichier binaire à partir de la base de données
    content = etudiant.content.read()
    
    # Créer une réponse HTTP avec le contenu du fichier en tant que téléchargement
    response = HttpResponse(content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % etudiant.cv
    return response

   

def etu_mes_stages(request):
    if request.method == 'GET':
        id_user = request.session.get('id_user', None)
        print("id_user=",id_user)
        if not Etudiants.objects.filter(id_user=id_user).exists():
            messages.success(request, "Vous n'avez postulé à aucun stage!")
            return render(request, 'etu_mes_stages.html')
        etudiant = Etudiants.objects.get(id_user=id_user)
        if not Candidatures.objects.filter(id_etu=etudiant.id_etu).exists():
            messages.success(request, "Vous n'avez postulé à aucun stage!")
            return render(request, 'etu_mes_stages.html')
            #return render(request, 'etu_mes_stages.html')
        liste_candidatures=Candidatures.objects.filter(id_etu=etudiant.id_etu)
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut).select_related('entreprise__utilisateur')
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut)
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut).select_related('entreprise__utilisateur')
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut).select_related('id_ent', 'id_ent__id_user')
        #candidatures = Candidatures.objects.all().select_related('id_offre')
        candidatures = Candidatures.objects.all().select_related('id_offre__id_ent__id_user')
        statuts = Candidatures.objects.all().select_related('id_offre__id_statut')
        liste_titres = {candidature.id_offre.titre_offre for candidature in candidatures}
        liste_localisations = {candidature.id_offre.localisation for candidature in candidatures}
        #liste_users = {candidature.id_offre.id_ent.id_user for candidature in candidatures}
        liste_noms = {candidature.id_offre.id_ent.id_user.nom for candidature in candidatures}
        liste_statuts = {candidature.id_statut.lib_statut for candidature in statuts}   
       
        context = {
            'liste_titres' : liste_titres,
            'liste_noms' : liste_noms,
            'liste_localisations' : liste_localisations,
            'liste_statuts' : liste_statuts
        }
        return render(request, 'etu_mes_stages.html',context)


    return render(request, 'etu_mes_stages.html')

def admin_creer_util(request):
    erreur = None
    # Récupération des infos de la table Profils pour afficher dans la liste de valeurs du formulaire
    profils = Profils.objects.all()
    if request.method == 'POST':
        id_profil= request.POST.get('id_profil')
        profil_u = Profils.objects.get(id_profil=id_profil)
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        num_tel = request.POST.get('num_tel')
        password = request.POST.get('password')
        num_voie = request.POST.get('num_voie')
        nom_voie = request.POST.get('nom_voie')
        code_postal = request.POST.get('code_postal')
        commune = request.POST.get('commune')
        if (profil_u.lib_profil == "Entreprise"):
            desc_ent = request.POST.get('desc_ent')
        else:
            prenom = request.POST.get('prenom')
        erreur=None
        if profil_u.lib_profil == "Entreprise" and not (nom and desc_ent and email and num_tel and password and num_voie and nom_voie and code_postal and commune and id_profil) :
             messages.error(request, "Tous les champs doivent être remplis.")
             return redirect('admin_creer_util') 
        if profil_u.lib_profil != "Entreprise" and not (nom and prenom and email and num_tel and password and num_voie and nom_voie and code_postal and commune and id_profil):
             messages.error(request, "Tous les champs doivent être remplis.")
             return redirect('admin_creer_util') 
        if not (num_tel.isdigit() and num_voie.isdigit() and code_postal.isdigit()):
            messages.error(request, "Le numéro de téléphone, le numéro de voie et le code postal doivent contenir uniquement des chiffres.")
            return redirect('admin_creer_util')
        if erreur:
            messages.error(request, erreur)
            return redirect('admin_creer_util')   
        # récupérer utilisateur si déjà existant à partir de son email
        utilisateur = Utilisateurs.objects.filter(email=email).first()
        if utilisateur:
            # renvoyer erreur "utilisateur déjà existant"
            messages.error(request, "Utilisateur déjà existant avec le même email")
            return redirect('admin_creer_util')
        
        # créer l'utilisateur en base
        # Positionnet le statut à Actif à la création de l'utilisateur
        statut_actif = Statuts.objects.get(lib_statut='A')
        profil=Profils.objects.get(id_profil=id_profil)
        if profil_u.lib_profil != "Entreprise":
            utilisateur = Utilisateurs(nom=nom, prenom=prenom, email=email, num_tel=num_tel, password=password, num_voie=num_voie, nom_voie=nom_voie, code_postal=code_postal, commune=commune, id_statut=statut_actif, id_profil=profil)
            utilisateur.save()
            messages.success(request, "Utilisateur créé avec succès!")
            return redirect('admin_creer_util')
        else:
            utilisateur = Utilisateurs(nom=nom, email=email, num_tel=num_tel, password=password, num_voie=num_voie, nom_voie=nom_voie, code_postal=code_postal, commune=commune, id_statut=statut_actif, id_profil=profil)
            utilisateur.save()
            # chercher id_user dans utilisateurs avec email pour valoriser desc_ent dans entreprises
            utilisateur = Utilisateurs.objects.filter(email=email).first()
            entreprise = Entreprises(id_user=utilisateur,desc_ent=desc_ent)
            entreprise.save()
            messages.success(request, "Utilisateur créé avec succès!")
            return redirect('admin_creer_util')
    
    return render(request, 'admin_creer_util.html', {'erreur':erreur,'profils':profils})


def admin_creer_util_succes(request):
     return render(request, 'admin_creer_util_succes.html')

def admin_modif_util(request):
    erreur = None
    # Récupération des infos de la table Profils pour afficher dans la liste de valeurs du formulaire
    utilisateurs = Utilisateurs.objects.all() 
    return render(request, 'admin_modif_util.html',{'erreur':erreur,'utilisateurs':utilisateurs})

def modifier_utilisateur(request):
     return render(request, 'modifier_utilisateur.html')

def admin_valider_offre(request):
    if request.method == 'GET':
        id_statut = Statuts.objects.get(lib_statut='EA')
        if not OffreStage.objects.filter(id_statut=id_statut).exists():
            messages.success(request, "Il n'existe aucune offre de stage à valider")
            return redirect('admin_modif_util')
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut)
        #offres_stage = OffreStage.objects.filter(id_statut=id_statut).select_related('entreprise__utilisateur')
        offres_stage = OffreStage.objects.filter(id_statut=id_statut).select_related('id_ent', 'id_ent__id_user')
        noms_utilisateurs = {offre.id_ent.id_user.nom for offre in offres_stage}
        context = {
            'offres_stage' : offres_stage,
            'noms_utilisateurs': noms_utilisateurs ,
        }
        return render(request, 'admin_valider_offre.html',context)
    if request.method == 'POST':
        if 'offres_stage' in request.POST:
            offres_stage_cochees = request.POST.getlist('offres_stage')
            id_statut = Statuts.objects.get(lib_statut='P')
            for offre_stage_id in offres_stage_cochees:
            # effectuer le traitement souhaité pour chaque article coché
                offre_stage = OffreStage.objects.get(id_offre=offre_stage_id)
                # mise en base de l'id_offre dans offre_stage avec statut='P'(publié)
                offre_stage.id_statut=id_statut
                offre_stage.save()
        messages.success(request, "Offres de stage validées avec succès!")
        return redirect('admin_modif_util')
                
                
        #return render(request, 'admin_valider_offre.html')
    
    return render(request, 'admin_valider_offre.html')



def deconnexion(request):
     request.session.flush()
     logout(request)
     messages.success(request, "Vous avez été déconnecté!")
     return render(request, 'accueil.html')


def admin_modifier(request):
    # Récupérer l'identifiant de l'utilisateur à modifier depuis l'URL
    
    if request.method == 'GET':
        id_user = request.GET.get('id')
        # Récupérer l'utilisateur correspondant à cet identifiant
        utilisateur = get_object_or_404(Utilisateurs, id_user=id_user)
        id_user = utilisateur.id_user
        nom = utilisateur.nom
        prenom= utilisateur.prenom
        email = utilisateur.email
        num_tel = utilisateur.num_tel
        num_voie = utilisateur.num_voie
        nom_voie = utilisateur.nom_voie
        code_postal = utilisateur.code_postal
        commune = utilisateur.commune
        mdp = utilisateur.password
        # Récupérer le libellé du profil de l'utilisateur
        lib_profil = utilisateur.id_profil.lib_profil
        lib_statut = utilisateur.id_statut.lib_statut
        # à gauche et à droite la variable python
        context = {
        'id_user': id_user,
        'lib_profil': lib_profil,
        'nom': nom,
        'prenom': prenom,
        'email': email,
        'num_tel': num_tel,
        'num_voie': num_voie,
        'nom_voie': nom_voie,
        'code_postal': code_postal,
        'commune':commune,
        'mdp': mdp,
        'lib_statut': lib_statut
        }
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        #utilisateur = Utilisateurs.objects.get(id_user=id_user)
        # Récupérer les valeurs des champs du formulaire
        #le paramètre dans le get est le id du champs dans le formulaire html
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        num_tel = request.POST.get('num_tel')
        num_voie = request.POST.get('num_voie')
        nom_voie = request.POST.get('nom_voie')
        code_postal = request.POST.get('code_postal')
        commune = request.POST.get('commune')
        mdp = request.POST.get('password')
        lib_statut = request.POST.get('statut')
        id_statut = Statuts.objects.get(lib_statut=lib_statut)
        lib_profil = request.POST.get('profil')

         # Vérifier que tous les champs sont remplis
        if not nom or not email or not num_tel or not num_voie or not nom_voie or not code_postal or not commune or not mdp:
            #messages.error(request, 'Veuillez remplir tous les champs.')
            erreur ="Veuillez remplir tous les champs."
            context = {
            'id_user': id_user,
            'lib_profil' : lib_profil,
            'nom': nom,
            'prenom': prenom,
            'email': email,
            'num_tel': num_tel,
            'num_voie': num_voie,
            'nom_voie': nom_voie,
            'code_postal': code_postal,
            'commune':commune,
            'mdp': mdp,
            'lib_statut': lib_statut,
            'erreur' : erreur
            }
            return render(request, 'admin_modifier.html', context)
            #return render(request, 'admin_modifier', context)

        # Vérifier que les champs numériques contiennent uniquement des chiffres
        if not (num_tel.isdigit() and num_voie.isdigit() and code_postal.isdigit()):
            #messages.error(request, 'Le numéro de téléphone, le numéro de voie et le code postal doivent contenir uniquement des chiffres.')
            erreur ="Le numéro de téléphone, le numéro de voie et le code postal doivent contenir uniquement des chiffres"
            context = {
            'id_user': id_user,
            'lib_profil' : lib_profil,
            'nom': nom,
            'prenom': prenom,
            'email': email,
            'num_tel': num_tel,
            'num_voie': num_voie,
            'nom_voie': nom_voie,
            'code_postal': code_postal,
            'commune':commune,
            'mdp': mdp,
            'lib_statut': lib_statut,
            'erreur' : erreur
            }

            return render(request, 'admin_modifier.html', context)

        
            #response = '<script>window.location.reload();</script>'
            #return HttpResponse(response)
        
        # Mettre à jour les valeurs de l'utilisateur
        #id_user = request.POST.get('id_user')
        utilisateur =Utilisateurs.objects.get(id_user=id_user)
        utilisateur.nom = nom
        utilisateur.prenom = prenom
        utilisateur.email = email
        utilisateur.num_tel = num_tel
        utilisateur.num_voie = num_voie
        utilisateur.nom_voie = nom_voie
        utilisateur.code_postal = code_postal
        utilisateur.commune = commune
        utilisateur.password=mdp
        lib_statut = request.POST.get('statut')
        utilisateur.id_statut = Statuts.objects.get(lib_statut=lib_statut)

        utilisateur.save()
      
        # Ajouter un message de confirmation
        messages.success(request, 'L\'utilisateur a été modifié avec succès.')

         # Fermer la fenêtre popup et rafraîchir la page parente
        response = '<script>window.close(); window.opener.location.reload();</script>'
        return HttpResponse(response)
        
    return render(request, 'admin_modifier.html', context)



def admin_confirm_modifier(request):
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        utilisateur = Utilisateurs.objects.get(id_user=id_user)

        # Récupérer les valeurs des champs du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        num_voie = request.POST.get('num_voie')
        nom_voie = request.POST.get('nom_voie')
        code_postal = request.POST.get('code_postal')
        commune = request.POST.get('commune')
        email = request.POST.get('email')
        num_tel = request.POST.get('num_tel')
        id_statut = request.POST.get('id_statut')
        id_profil = request.POST.get('id_profil')

        # Mettre à jour les valeurs de l'utilisateur
        utilisateur.nom = nom
        utilisateur.prenom = prenom
        utilisateur.num_voie = num_voie
        utilisateur.nom_voie = nom_voie
        utilisateur.code_postal = code_postal
        utilisateur.commune = commune
        utilisateur.email = email
        utilisateur.num_tel = num_tel
        utilisateur.id_statut = id_statut
        utilisateur.id_profil = id_profil
        utilisateur.save()

       
       
        # Ajouter un message de confirmation
        messages.success(request, 'L\'utilisateur a été modifié avec succès.')

        # Rediriger vers la page admin_modif_util.html pour afficher les changements
        return redirect('admin_modif_util')