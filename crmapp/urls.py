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

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs


    # Admin URL


    # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs

)
