from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('test',views.testchuanshu),
    path('sheji',views.sheji),
    path('liaotian',views.liaotian),
    path('shejiliaotian',views.shejiliaotian),
    path('shengchengduihua',views.shengchengduihua),
]