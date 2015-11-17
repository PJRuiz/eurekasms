from django.conf.urls import patterns, url

contact_urls = patterns('',
	url(r'^contact/new/$',
    	'crmapp.contacts.views.contact_cru', name='contact_new'
	),
    url(r'^$', 
    	'crmapp.contacts.views.contact_detail', name="contact_detail"
    ),

)