from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-exam/', views.add_exam, name='add_exam'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
    path('query3/', views.query3, name='query3'),
    path('', views.home, name='home'),  # Root URL
]
