# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from collections import OrderedDict
from rest_framework.exceptions import NotFound
from pyzabbix import ZabbixAPI
from django.contrib.auth.models import User

# 登陆zabbix
zabbix = ZabbixAPI(settings.ZABBIX_SERVER)
zabbix.login(settings.ZABBIX['user'], settings.ZABBIX['password'])


# 成功请求
class OkResponse(Response):
    def __init__(self, data=None, **kwargs):
        _data = {}
        if data:
            _data['data'] = data
        _data['code'] = 200
        _data['msg'] = 'success'
        super().__init__(_data, **kwargs)


# 失败请求
class FailResponse(Response):
    def __init__(self, data=None, code=40000, msg='fail', **kwargs):
        _data = {}
        if data:
            _data['data'] = data
        _data['code'] = code
        _data['msg'] = msg
        super().__init__(_data, **kwargs)


def _positive_int(integer_string, strict=False, cutoff=None):
    """
    Cast a string to a strictly positive integer.
    """
    ret = int(integer_string)
    if ret < 0 or (ret == 0 and strict):
        raise ValueError()
    if cutoff:
        return min(ret, cutoff)
    return ret


# 分页功能
class CustomPageNumberPagination(PageNumberPagination):
    def __init__(self,
                 page_size_query_param=100,
                 page_query_param=1,
                 page_size=100,
                 max_page_size=1000):
        self.page_size = page_size
        self.page_size_query_param = page_size_query_param
        self.page_query_param = page_query_param
        self.max_page_size = max_page_size

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                return _positive_int(self.page_size_query_param,
                                     strict=True,
                                     cutoff=self.max_page_size)
            except (KeyError, ValueError):
                pass

        return self.page_size

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.page_query_param
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            msg = self.invalid_page_message.format(page_number=page_number,
                                                   message=str(exc))
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data, request):
        return Response(
            OrderedDict([('count', self.page.paginator.count),
                         ('pageSize', self.get_page_size(request)),
                         ('page', self.page_query_param), ('results', data)]))


# 主机
class zabbixHost(APIView):
    def get(self, request):
        try:
            host_list = zabbix.host.get(output="extend")
            for i in host_list:
                hostinterface = zabbix.hostinterface.get(output="extend",
                                                         hostids=i['hostid'])
                i['ip'] = hostinterface[0]['ip']
                i['dns'] = hostinterface[0]['dns']
                i['port'] = hostinterface[0]['port']
                templates = zabbix.template.get(output=["templateid"],
                                                hostids=i['hostid'])
                i['templateids'] = templates
                hostgroupids = zabbix.hostgroup.get(output=["groupid"],
                                                    hostids=i['hostid'])
                i['hostgroupids'] = hostgroupids
            return OkResponse(data=host_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def post(self, request):
        try:
            host = request.data['hostname']
            ip = request.data["ip"]
            port = request.data["port"]
            groupid = request.data['groupid']
            templateid = request.data['templateid']
            templates = []
            for i in templateid:
                templates.append({"templateid": i})
            host_list = zabbix.host.create(host=host,
                                           interfaces=[{
                                               "type": 1,
                                               "main": 1,
                                               "useip": 1,
                                               "ip": ip,
                                               "dns": "",
                                               "port": port
                                           }],
                                           groups=[{
                                               "groupid": groupid
                                           }],
                                           templates=templates)
            return OkResponse(data=host_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def put(self, request):
        try:
            host = request.data['hostname']
            hostid = request.data['hostid']
            ip = request.data["ip"]
            port = request.data["port"]
            groupid = request.data['groupid']
            templateid = request.data['templateid']
            templates = []
            for i in templateid:
                templates.append({'templateid': i})
            hostinterface_id = zabbix.hostinterface.get(
                output="output", hostids=hostid)[0]['interfaceid']
            zabbix.hostinterface.update(interfaceid=hostinterface_id,
                                        ip=ip,
                                        port=port)
            host_list = zabbix.host.update(host=host,
                                           hostid=hostid,
                                           groups=[{
                                               'groupid': groupid
                                           }],
                                           templates=templates)
            return OkResponse(data=host_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def delete(self, request):
        try:
            hostid = request.data['hostid']
            host_list = zabbix.host.delete(hostid)
            return OkResponse(data=host_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 主机group
class zabbixhostGroup(APIView):
    def get(self, request):
        try:
            hostgroup_list = zabbix.hostgroup.get(output="extend",
                                                  sortorder='groupid')
            for i in hostgroup_list:
                host = zabbix.host.get(output=["host"], groupids=i['groupid'])
                i['hosts'] = host
            hostgroup_list.reverse()
            return OkResponse(data=hostgroup_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def post(self, request):
        try:
            hostgroup_name = request.data['name']
            hostgroup_list = zabbix.hostgroup.create(name=hostgroup_name)
            return OkResponse(data=hostgroup_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def put(self, request):
        try:
            groupid = request.data['groupid']
            hostgroup_name = request.data['name']
            hostgroup_list = zabbix.hostgroup.update(name=hostgroup_name,
                                                     groupid=groupid)
            return OkResponse(data=hostgroup_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def delete(self, request):
        try:
            groupid = request.data['groupid']
            hostgroup_list = zabbix.hostgroup.delete(groupid)
            return OkResponse(data=hostgroup_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取主机下应用程序
class zabbixHostapplication(APIView):
    def get(self, request, host_id):
        try:
            application_list = zabbix.application.get(
                hostids=host_id,
                output="extend",
            )
            return OkResponse(data=application_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def post(self, request, host_id):
        try:
            name = request.data['name']
            application_list = zabbix.application.create(name=name,
                                                         hostid=host_id)
            return OkResponse(data=application_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def put(self, request, host_id):
        try:
            name = request.data['name']
            applicationid = request.data['applicationid']
            application_list = zabbix.application.update(
                name=name, applicationid=applicationid)
            return OkResponse(data=application_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def delete(self, request, host_id):
        try:
            applicationid = request.data['applicationid']
            application_list = zabbix.application.delete(applicationid)
            return OkResponse(data=application_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取主机应用下监控项
class zabbixHostitem(APIView):
    def get(self, request, host_id, application_id):
        try:
            item_list = zabbix.item.get(
                hostids=host_id,
                applicationids=application_id,
                output="extend",
            )
            return OkResponse(data=item_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def post(self, request, host_id, application_id):
        try:
            name = request.data['name']
            key_ = request.data['key_']
            type = 0
            value_type = 3
            interfaceid = zabbix.hostinterface.get(
                output="output", hostids=host_id)[0]['interfaceid']
            delay = "30s"
            item_list = zabbix.item.create(name=name,
                                           key_=key_,
                                           hostid=host_id,
                                           type=type,
                                           value_type=value_type,
                                           interfaceid=interfaceid,
                                           applications=[str(application_id)],
                                           delay=delay)
            return OkResponse(data=item_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def delete(self, request, host_id, application_id):
        try:
            itemid = request.data['itemid']
            item_list = zabbix.item.delete(itemid)
            return OkResponse(data=item_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def put(self, request, host_id, application_id):
        try:
            itemid = request.data['itemid']
            name = request.data['name']
            key_ = request.data['key_']
            item_list = zabbix.item.update(itemid=itemid, name=name, key_=key_)
            return OkResponse(data=item_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取模板template
class zabbixtemplate(APIView):
    def get(self, request):
        try:
            template_list = zabbix.template.get(
                output=["host", "name", "templateid", "description"])
            return OkResponse(data=template_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取模板下应用项
class zabbixTemplaterapplication(APIView):
    def get(self, request, template_id):
        try:
            templaterapplication = zabbix.application.get(
                output="extend", templateids=template_id)
            return OkResponse(data=templaterapplication)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取模板下item
class zabbixTemplateitem(APIView):
    def get(self, request, template_id, application_id):
        try:
            templateritem = zabbix.item.get(output="extend",
                                            templateids=template_id,
                                            applicationids=application_id)
            return OkResponse(data=templateritem)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取主机触发器
class zabbixTriger(APIView):
    def get(self, request, host_id):
        try:
            trigger_list = zabbix.trigger.get(output="extend", hostids=host_id)
            return OkResponse(data=trigger_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def post(self, request, host_id):
        try:
            dedescription = request.data['description']
            expression = request.data['expression']
            priority = request.data['priority']
            trigger_list = zabbix.trigger.create(hostids=host_id,
                                                 description=dedescription,
                                                 expression=expression,
                                                 priority=priority)
            return OkResponse(data=trigger_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def put(self, request, host_id):
        try:
            triggerid = request.data['triggerid']
            description = request.data['description']
            expression = request.data['expression']
            priority = request.data['priority']
            trigger_list = zabbix.trigger.update(
                hostids=host_id,
                triggerid=triggerid,
                description=description,
                expression=expression,
                priority=priority,
            )
            return OkResponse(data=trigger_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))

    def delete(self, request, host_id):
        try:
            triggerid = request.data['triggerid']
            trigger_list = zabbix.trigger.delete(triggerid=triggerid)
            return OkResponse(data=trigger_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取系统默认监控项key
class zabbixItemkey(APIView):
    def get(self, request):
        try:
            Itemkey_list = zabbix.item.get(output=["key_"])
            return OkResponse(data=Itemkey_list)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))


# 获取当前报警
class zabbixcurrentIssue(APIView):
    def get(self, request):
        try:
            # Get a list of all issues (AKA tripped triggers)
            triggers = zabbix.trigger.get(
                only_true=1,
                skipDependent=1,
                monitored=1,
                active=1,
                output='extend',
                expandDescription=1,
                selectHosts=['host'],
            )

            # Do another query to find out which issues are Unacknowledged
            unack_triggers = zabbix.trigger.get(
                only_true=1,
                skipDependent=1,
                monitored=1,
                active=1,
                output='extend',
                expandDescription=1,
                selectHosts=['host'],
                withLastEventUnacknowledged=1,
            )
            unack_trigger_ids = [t['triggerid'] for t in unack_triggers]
            for t in triggers:
                t['unacknowledged'] = True if t['triggerid'] in unack_trigger_ids \
                    else False

            # Print a list containing only "tripped" triggers
            result = []
            for t in triggers:
                f = {}
                if int(t['value']) == 1:
                    f['host'] = t['hosts'][0]['host']
                    f['description'] = t['description']
                    f['unacknowledged'] = '(Unack)' if t[
                        'unacknowledged'] else ''
            return OkResponse(data=result)
        except Exception as identifier:
            return FailResponse(msg=str(identifier))
