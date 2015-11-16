from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact-list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', views.ContactDetail.as_view(), name='contact-detail'),

]