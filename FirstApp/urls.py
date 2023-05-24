from django.urls import include, re_path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^course/$',views.courseListView.as_view(), name='course'),
    re_path(r'course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='Данные о курсе'),
    re_path(r'teacher/$', views.teacherListView.as_view(), name='teacher'),
    re_path(r'teacher/(?P<pk>\d+)$', views.teacherDetailView.as_view(), name='Данные о преподавателе'),
] 

