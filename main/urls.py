from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^game/$',views.newgame,name='newgame'),
    url(r'^joingame/$', views.joingame, name='joingame'),
    url(r'^game/(?P<token>[0-9]+)$',views.game,name='game'),
    url(r'^update/$',views.update_board,name='update_board'),
    url(r'^refresh/$',views.refresh,name='refresh')
]
