from django.conf.urls import url
from rest import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact-list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', views.ContactDetail.as_view(), name='contact-detail'),

    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[^/]+)/$', views.TagDetail.as_view(), name='tag-detail'),
]