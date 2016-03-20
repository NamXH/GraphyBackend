from django.conf.urls import url
from rest import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact-list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', views.ContactDetail.as_view(), name='contact-detail'),

    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[^/]+)/$', views.TagDetail.as_view(), name='tag-detail'),

    url(r'^relationship_types/$', views.RelationshipTypeList.as_view(), name='relationship_types-list'),
    url(r'^relationship_types/(?P<pk>[^/]+)/$', views.RelationshipTypeDetail.as_view(), name='relationship_types-detail'),

    url(r'^contact_tag_maps/$', views.ContactTagMapList.as_view(), name='contact_tag_map-list'),
    url(r'^contact_tag_maps/(?P<pk>[^/]+)/$', views.ContactTagMapDetail.as_view(), name='contact_tag_map-detail'),

    url(r'^relationships/$', views.RelationshipList.as_view(), name='relationship-list'),
    url(r'^relationships/(?P<pk>[^/]+)/$', views.RelationshipDetail.as_view(), name='relationship-detail'),

    url(r'^phone_numbers/$', views.PhoneNumberList.as_view(), name='phone_number-list'),
    url(r'^phone_numbers/(?P<pk>[^/]+)/$', views.PhoneNumberDetail.as_view(), name='phone_number-detail'),

    url(r'^addresses/$', views.AddressList.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[^/]+)/$', views.AddressDetail.as_view(), name='address-detail'),

    # url(r'^urls/$', views.TagList.as_view(), name='url-list'),
    # url(r'^urls/(?P<pk>[^/]+)/$', views.TagDetail.as_view(), name='url-detail'),

    url(r'^emails/$', views.EmailList.as_view(), name='email-list'),
    url(r'^emails/(?P<pk>[^/]+)/$', views.EmailDetail.as_view(), name='email-detail'),

    url(r'^special_dates/$', views.SpecialDateList.as_view(), name='special_date-list'),
    url(r'^special_dates/(?P<pk>[^/]+)/$', views.SpecialDateDetail.as_view(), name='special_date-detail'),

    url(r'^instant_messages/$', views.InstantMessageList.as_view(), name='instant_message-list'),
    url(r'^instant_messages/(?P<pk>[^/]+)/$', views.InstantMessageDetail.as_view(), name='instant_message-detail'),
]