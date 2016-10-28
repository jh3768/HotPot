from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^authlogin/', views.auth_and_login, name='authlogin'),
    url(r'^authsignup/', views.auth_and_signup, name='authsignup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post', views.post, name='post'),
    url(r'^delete', views.delete, name='delete'),
]
