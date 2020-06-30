from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name="home"),
    path('port/<slug:port_slug>', views.port, name="port")
]
