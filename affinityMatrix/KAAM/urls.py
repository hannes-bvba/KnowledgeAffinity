from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^dotest', views.dotest, name='dotest'),
    url( r'^matrix1/',views.KnowledgeAndAffinityMatrix1, name='matrix'),
    url( r'^matrix/',views.KnowledgeAndAffinityMatrix, name='matrix'),
    url( r'^SkillUp/(?P<skillID>\d+)/$', views.SkillUp, name="SkillUp"),
    url(r'^SkillDown/(?P<skillID>\d+)/$', views.SkillDown, name="SkillDown"),
    url(r'^AffinityUp/(?P<skillID>\d+)/$', views.AffinityUp, name="AffinityUp"),
    url(r'^AffinityDown/(?P<skillID>\d+)/$', views.AffinityDown, name="AffinityDown"),
    url(r'^createAccount/$', views.createAccount, name='createAccount'),
    url(r'^addSkillToTeam/$', views.addSkillToTeam, name='addSkillToTeam'),
    url(r'^addNewSkillToTeam/$', views.addNewSkillToTeam, name='addNewSkillToTeam'),
    url(r'^removeSkillFromTeam/(?P<skillId>\d+)/$', views.removeSkillFromTeam, name="removeSkillFromTeam"),




]




