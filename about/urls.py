from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
]
