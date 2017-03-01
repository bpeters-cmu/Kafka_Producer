from django.conf.urls import url

from . import views

app_name = 'twitter'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^status/$', views.process, name='process'),
]