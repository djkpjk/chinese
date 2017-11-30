from django.conf.urls import url
from memorization import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^lesson/(?P<lesson>\d+)/$', views.lesson_base, name='lesson_base'),
    url(r'^lesson/(?P<lesson>\d+)/quiz/$', views.quiz, name='quiz'),
]

