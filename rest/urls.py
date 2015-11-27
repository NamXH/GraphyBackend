from django.conf.urls import url
from rest import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact-list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', views.ContactDetail.as_view(), name='contact-detail'),
]