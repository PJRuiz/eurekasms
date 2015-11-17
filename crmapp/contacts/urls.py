from django.conf.urls import patterns, url
from .views import ContactDelete


contact_urls = patterns('',

    url(r'^$', 
    	'crmapp.contacts.views.contact_detail', name="contact_detail"
    ),
    url(r'^contact/(?P<pk>[\w-]+)/delete/$',
    	ContactDelete.as_view(), name='contact_delete'
	),

)