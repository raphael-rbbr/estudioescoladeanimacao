from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateInscriprion, name="index"),
    path("list/", views.ListInscriprion, name="list"),
    path("sucesso/", views.InscriptionSucess, name="sucesso"),
    path('inscription_csv', views.inscription_csv, name='inscription_csv'),
    path('inscription_excel', views.inscription_excel, name='inscription_excel'),
    path('<pk>/inscription_pdf', views.inscription_pdf, name='inscription_pdf'),
    path("up", views.Return200, name='return200')
    # path('<pk>/', views.InscriptionDetailView.as_view()),

]
