from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('main/<str:pk>/', views.main, name="main"),
    path('create_anomaly/', views.createAnomaly, name="create_anomaly"),
    path('update_anomaly/<str:pk>/', views.updateAnomaly, name="update_anomaly"),
    path('delete_anomaly/<str:pk>/', views.deleteAnomaly, name="delete_anomaly"),
    path('anom/<str:pk>/', views.anom, name="anom"),
    path('pdf/<str:pk>/', views.render_pdf_anom, name='pdf'),
    path('export/<str:pk>/', views.export, name="export"),
]
