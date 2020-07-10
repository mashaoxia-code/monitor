from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import zabbixHost, zabbixHostapplication, zabbixHostitem, zabbixcurrentIssue, zabbixTriger, zabbixhostGroup, zabbixtemplate, zabbixItemkey, zabbixTemplaterapplication, zabbixTemplateitem

urlpatterns = [
    url(r'^v1/currentIsuue$', zabbixcurrentIssue.as_view()),  # 获取出错信息(get, post)
    url(r'^v1/itemkey$', zabbixItemkey.as_view()),  # 获取主机信息(get)
    url(r'^v1/hostgroup$', zabbixhostGroup.as_view()),  # 获取主机组信息(get, post, put, delete)

    url(r'^v1/host$', zabbixHost.as_view()),  # 获取主机信息(get)
    url(r'^v1/host/(?P<host_id>[a-zA-Z0-9]+)/application$', zabbixHostapplication.as_view()),  # 获取主机下应用(get)
    url(r'^v1/host/(?P<host_id>[a-zA-Z0-9]+)/trigger$', zabbixTriger.as_view()),  # 获取触发器(get)
    url(r'^v1/host/(?P<host_id>[a-zA-Z0-9]+)/application/(?P<application_id>[a-zA-Z0-9]+)/item$', zabbixHostitem.as_view()),  # 获取主机下应用监控项(get)

    url(r'^v1/template$', zabbixtemplate.as_view()),  # 获取模板template(get)
    url(r'^v1/template/(?P<template_id>[a-zA-Z0-9]+)/application$', zabbixTemplaterapplication.as_view()),  # 获取模板template(get)
    url(r'^v1/template/(?P<template_id>[a-zA-Z0-9]+)/application/(?P<application_id>[a-zA-Z0-9]+)/item$', zabbixTemplateitem.as_view()),  # 获取模板template(get)
]
urlpatterns = format_suffix_patterns(urlpatterns)
