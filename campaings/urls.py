from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateInscriprion, name="index"),
    path("list", views.ListInscriprion, name="list"),
    path('inscription_csv', views.inscription_csv, name='inscription_csv'),
    path('/<pk>/inscription_pdf', views.inscription_pdf, name='inscription_pdf'),
    # path('<pk>/', views.InscriptionDetailView.as_view()),

]
