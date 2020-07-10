### 接口描述
    获取主机应用下监控项
#### HTTP方法: GET

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application/[application_id]/item


#### 请求参数
    无
    
#### 返回示例
    {
        "data": [
            {
                "itemid": "30644",
                "type": "5",
                "snmp_community": "",
                "snmp_oid": "",
                "hostid": "10321",
                "name": "Zabbix agent availability",
                "key_": "zabbix[host,agent,available]",
                "delay": "1m",
                "history": "7d",
                "trends": "365d",
                "status": "0",
                "value_type": "3",
                "trapper_hosts": "",
                "units": "",
                "snmpv3_securityname": "",
                "snmpv3_securitylevel": "0",
                "snmpv3_authpassphrase": "",
                "snmpv3_privpassphrase": "",
                "formula": "",
                "logtimefmt": "",
                "templateid": "29544",
                "valuemapid": "22",
                "params": "",
                "ipmi_sensor": "",
                "authtype": "0",
                "username": "",
                "password": "",
                "publickey": "",
                "privatekey": "",
                "flags": "0",
                "interfaceid": "0",
                "port": "",
                "description": "Monitoring agent availability status",
                "inventory_link": "0",
                "lifetime": "30d",
                "snmpv3_authprotocol": "0",
                "snmpv3_privprotocol": "0",
                "snmpv3_contextname": "",
                "evaltype": "0",
                "jmx_endpoint": "",
                "master_itemid": "0",
                "timeout": "3s",
                "url": "",
                "query_fields": [],
                "posts": "",
                "status_codes": "200",
                "follow_redirects": "1",
                "post_type": "0",
                "http_proxy": "",
                "headers": [],
                "retrieve_mode": "0",
                "request_method": "0",
                "output_format": "0",
                "ssl_cert_file": "",
                "ssl_key_file": "",
                "ssl_key_password": "",
                "verify_peer": "0",
                "verify_host": "0",
                "allow_traps": "0",
                "state": "0",
                "error": "",
                "lastclock": "1584064784",
                "lastns": "767871826",
                "lastvalue": "0",
                "prevvalue": "0"
            }
        ],
        "code": 200,
        "msg": "success"
    }

-----------------------------
### 接口描述
    添加主机应用项下监控项
#### HTTP方法: 
    POST

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application/[application_id]/item


#### 请求参数
    {
        "name": "test",
        "key_": "jkej"
    }
    
#### 返回示例
    {
        "data": {
            "applicationids": [
                "1348"
            ]
        },
        "code": 200,
        "msg": "success"
    }

-----------------------------------
### 接口描述
    修改主机下应用项
#### HTTP方法: 
    PUT

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application/[application_id]/item


#### 请求参数
    {
        "itemid": 30753,
        "name": "test1",
        "key_": "jkej"
    }
    
#### 返回示例
    {
        "data": {
            "itemids": [
                30753
            ]
        },
        "code": 200,
        "msg": "success"
    }

-----------------------------

### 接口描述
    删除主机监控项
#### HTTP方法: 
    DELETE

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application/[application_id]/item


#### 请求参数
    {
        "itemid": "30751"
    }
    
#### 返回示例
    {
        "data": {
            "itemids": [
                "30751"
            ]
        },
        "code": 200,
        "msg": "success"
    }