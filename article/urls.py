from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Panel/Catagury/$',views._CatManage,name="_CatManage"),
    url(r'^Panel/(?P<cat>.*)se/(?P<ArtId>.*)se/$',views._Art_Detail,name="_Art_Detail"),
    url(r'^Panel/Cat:delete_(?P<pk>\d+)_/$',views.CatDel,name="CatDel"),
    url(r'^Panel/Arts/(?P<artID>.*)/$',views.ArticleAdmin,name="ArticleAdmin"),
    url(r'^Panel/Art:delete_(?P<pk>\d+)_/$',views.ArtDel,name="ArtDel"),
    url(r'^Arts/$',views.Articlepage,name="Articlepage"),
    url(r'^Arts/(?P<ArtId>.*)/$',views.ArticleDetail,name="ArticleDetail"),
    url(r'^Article/(?P<catt>.*)s/$',views.Catpage,name="Catpage"),
   
     ]
