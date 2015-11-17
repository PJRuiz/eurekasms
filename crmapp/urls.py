"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import HomePage
from accounts.views import AccountList
from accounts.urls import account_urls
from contacts.urls import contact_urls
from communications.urls import comm_urls



admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs

    url(r'^signup/$','subscribers.views.subscriber_new', name='sub_new'),


    # Admin URL
    (r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    (r'^login/$',
        'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}
    ),
    (r'^logout/$',
        'django.contrib.auth.views.logout', 
        {'next_page': '/login/'}
    ),

    # Account related URLs

    url(r'^account/new/$',
        'crmapp.accounts.views.account_cru', name='account_new'
    ),

    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'
    ),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
    # Contact related URLS
    url(r'^contact/new/$',
    'crmapp.contacts.views.contact_cru', name='contact_new'
),
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),


    # Communication related URLs
    url(r'^comm/new/$',
        'crmapp.communications.views.comm_cru', name='comm_new'
    ),
    url(r'^comm/(?P<uuid>[\w-]+)/', 
        include(comm_urls)
    ),


)
