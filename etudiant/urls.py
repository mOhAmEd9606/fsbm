from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^Etudiant/$',views.Etudiant,name="Etudiant"),
      url(r'^Physique/$',views.PhysiquePage,name="PhysiquePage"),
      url(r'^Physique/(?P<sem>.*)-ID!(?P<pk>\d+)/$',views.physiqueSemmester,name="physiqueSemmester"),
      url(r'^Physique/(?P<sem>.*)/(?P<modl>.*)/$',views.physiqueModulePage,name="physiqueModulePage"),
      url(r'^Physique-Search_/$',views.SearchPhysiquePage,name="SearchPhysiquePage"),
      url(r'^Physique/search/$',views.Search_MOdule,name="Search_MOdule"),

       url(r'^Chimie/$',views.ChimiePage,name="ChimiePage"),
      url(r'^Chimie/(?P<sem>.*)-ID!(?P<pk>\d+)/$',views.ChimieSemmester,name="ChimieSemmester"),
      url(r'^Chimie/(?P<sem>.*)/(?P<modl>.*)/$',views.ChimieModulePage,name="ChimieModulePage"),
      url(r'^Chimie-Search_/$',views.SearchChimiePage,name="SearchChimiePage"),
      url(r'^Chimie/search/$',views.Search_MOdule,name="Search_MOdule"),

        #___Filier
    url(r'^Panel/filier:list/$',views.filerList,name="filerList"),
    url(r'^Panel/filier:add/$',views.filierAdd,name="filierAdd"),
    url(r'^Panel/filier:edit(?P<pk>\d+)_/$',views.filierEdit,name="filierEdit"),
    url(r'^Panel/filier:delete(?P<pk>\d+)_/$',views.filierDel, name="filierDel"),
        # __Semmester
     url(r'^Panel/semmester:list/$',views.semmesterList, name="semmesterList"),
    url(r'^Panel/semmester:add/$',views.semmesterAdd,name="semmesterAdd"),
    # url(r'^Panel/semmester:edit (?P<name>.*)pk:(?P<pk>\d+)/$',views.semmesterEdit,name="semmesterEdit"),
    url(r'^Panel/semmester:delete_(?P<pk>\d+)_/$',views.semmesterDel,name="semmesterDel"),
    #     #__Module
      url(r'^Panel/module:list/$',views.moduleList,name="moduleList"),
       url(r'^Panel/module:add/$',views.moduleAdd,name="moduleAdd"),
      url(r'^Panel/module:delete(?P<pk>\d+)/$',views.moduleeDel,name="moduleeDel"),


      url(r'^Panel/CoureManageName:/(?P<modl>.*)-Idjfh(?P<pk>\d+)msb/$',views.coureAdmin,name="coureAdmin"),
      url(r'^Panel/Coure:delete(?P<pk>\d+)/$',views.moduleDel,name="moduleDel"),

      url(r'^Panel/TdsManageName:/(?P<modl>.*)-Idjfh(?P<pk>\d+)msb/$',views.TdsAdmin,name="TdsAdmin"),
      url(r'^Panel/td:delete_(?P<pk>\d+)_/$',views.tdDel,name="tdDel"),


       url(r'^Panel/TpsManageName:/(?P<modl>.*)-Idjfh(?P<pk>\d+)msb/$',views.TpsAdmin,name="TpsAdmin"),
      url(r'^Panel/tp:delete_(?P<pk>\d+)_/$',views.tpDel,name="tpDel"),
   
      url(r'^Panel/ExamsManageName:/(?P<modl>.*)-Idjfh(?P<pk>\d+)msb/$',views.examsAdmin,name="examsAdmin"),
      url(r'^Panel/exam:delete_(?P<pk>\d+)_/$',views.examDel,name="examDel"),
    
]
