### 接口描述
    获取所有主机
#### HTTP方法: GET

#### 请求URL: 
    [ip]:8000/v1/host


#### 请求参数
    无
    
#### 返回示例
    {
        "data": [
            {
                "hostid": "10318",
                "proxy_hostid": "0",
                "host": "Zabbix server",
                "status": "0",
                "disable_until": "0",
                "error": "",
                "available": "1",
                "errors_from": "0",
                "lastaccess": "0",
                "ipmi_authtype": "-1",
                "ipmi_privilege": "2",
                "ipmi_username": "",
                "ipmi_password": "",
                "ipmi_disable_until": "0",
                "ipmi_available": "0",
                "snmp_disable_until": "0",
                "snmp_available": "0",
                "maintenanceid": "0",
                "maintenance_status": "0",
                "maintenance_type": "0",
                "maintenance_from": "0",
                "ipmi_errors_from": "0",
                "snmp_errors_from": "0",
                "ipmi_error": "",
                "snmp_error": "",
                "jmx_disable_until": "0",
                "jmx_available": "0",
                "jmx_errors_from": "0",
                "jmx_error": "",
                "name": "Zabbix server",
                "flags": "0",
                "templateid": "0",
                "description": "",
                "tls_connect": "1",
                "tls_accept": "1",
                "tls_issuer": "",
                "tls_subject": "",
                "tls_psk_identity": "",
                "tls_psk": "",
                "proxy_address": "",
                "auto_compress": "1",
                "inventory_mode": "-1"
            }
        ],
        "code": 200,
        "msg": "success"
    }
---------------------------------------

### 接口描述
    增加主机
#### HTTP方法: POST

#### 请求URL: 
    [ip]:8000/v1/host


#### 请求参数
    {
        "hostname":"zabbix_test",
        "ip": "192.168.1.168",
        "port": 10050,
        "groupid": 2,
        "templateid": [10047]
    }
    
#### 返回示例
    {
        "data": {
            "hostids": [
                "10325"
            ]
        },
        "code": 200,
        "msg": "success"
    }
------------------------
### 接口描述
    修改主机
#### HTTP方法: 
    PUT

#### 请求URL: 
    [ip]:8000/v1/host

#### 请求参数
    {
        "hostname":"zabbix_test",
        "ip": "192.168.1.168",
        "port": 10050,
        "groupid": 2,
        "templateid": 10047,
        "hostid": 10325
    }
    
#### 返回示例
    {
        "data": {
            "hostids": [
                "10325"
            ]
        },
        "code": 200,
        "msg": "success"
    }

---------------------------
### 接口描述
    删除主机
#### HTTP方法: 
    DELETE

#### 请求URL: 
    [ip]:8000/v1/host

#### 请求参数
    {
        "hostid": 10325
    }
    
#### 返回示例
    {
        "data": {
            "hostids": [
                "10325"
            ]
        },
        "code": 200,
        "msg": "success"
    }

