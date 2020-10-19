from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^Panel/$',views.panel,name='panel'),
    url(r'^login/$',views.loginPage,name='loginPage'),
     url(r'^register/$',views.registerPage,name='registerPage'),
     path('logout/', views.logoutUser, name="logout"),
     url(r'^newsletter/add/$', views.news_letter, name='news_letter'),
]