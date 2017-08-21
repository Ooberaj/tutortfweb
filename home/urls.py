from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^programs/$',views.programs, name='programs'),
    url(r'^team/$',views.team, name='team'),
    url(r'^about/$',views.about, name='about'),
    url(r'^student_signup/$',views.student_forms, name='student'),
    url(r'^teacher_signup/$',views.teacher_forms, name='teacher'),
]
