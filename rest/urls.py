from django.conf.urls import url
from rest import views

urlpatterns = [
    url(r'^tags/$', views.TagList.as_view()),
]