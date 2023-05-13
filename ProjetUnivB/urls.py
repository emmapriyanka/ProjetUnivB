"""
URL configuration for ProjetUnivB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppliUnivB import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('etu_chercher_stage/etu_mon_profil', views.etu_mon_profil, name='etu_mon_profil'),
    path('etu_chercher_stage/etu_mes_stages', views.etu_mes_stages, name='etu_mes_stages'),
    path('etu_chercher_stage/etu_chercher_stage', views.etu_chercher_stage, name='etu_chercher_stage'),
    path('etu_chercher_stage/accueil', views.deconnexion, name='deconnexion'),
    path('etu_chercher_stage/etu_postuler_stage', views.etu_chercher_stage, name='etu_chercher_stage'),
    path('etu_chercher_stage/', views.etu_chercher_stage, name='etu_chercher_stage'),
    path('etu_postuler_stage', views.etu_postuler_stage, name='etu_postuler_stage'),
    path('etu_mon_profil', views.etu_mon_profil, name='etu_mon_profil'),
    path('etu_mes_stages/', views.etu_mes_stages, name='etu_mes_stages'),
    path('ent_publier_offre', views.ent_publier_offre, name='ent_publier_offre'),
    path('ent_publier_offre/', views.ent_publier_offre, name='ent_publier_offre'),
    path('ent_publier_offre/ent_publier_offre', views.ent_publier_offre, name='ent_publier_offre'),
    path('ent_publier_offre/ent_consult_cand', views.ent_consult_cand, name='ent_consult_cand'),
    path('ent_publier_offre/ent_mon_profil', views.ent_mon_profil, name='ent_mon_profil'),
    path('ent_publier_offre/accueil', views.deconnexion, name='deconnexion'),
    path('ent_consult_cand', views.ent_consult_cand, name='ent_consult_cand'),
    path('ent_mon_profil', views.ent_mon_profil, name='ent_mon_profil'),
    path('admin_creer_util', views.admin_creer_util, name='admin_creer_util'),
    path('admin_creer_util_succes', views.admin_creer_util_succes, name='admin_creer_util_succes'),
    path('admin_modif_util', views.admin_modif_util, name='admin_modif_util'),
    path('admin_modifier', views.admin_modifier, name='admin_modifier'),
    path('admin_valider_offre', views.admin_valider_offre, name='admin_valider_offre'),
    path('accueil', views.deconnexion, name='deconnexion'),
    path('admin_confirm_modifier', views.admin_confirm_modifier, name='admin_confirm_modifier'),
    path('etudiant/<int:etudiant_id>/cv/', views.download_cv, name='download_cv'),
    path('etudiant/<int:etudiant_id>/lm/', views.download_lm, name='download_lm'),
]