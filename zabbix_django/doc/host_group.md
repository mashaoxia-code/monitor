### 接口描述
    获取所有主机组
#### HTTP方法: 
    GET
#### 请求URL: 
    [ip]:8000/v1/hostgroup

#### 请求参数
    无
#### 返回示例
    {
        "data": [
            {
                "groupid": "1",
                "name": "Templates",
                "internal": "0",
                "flags": "0",
                "hosts": []
            },
            {
                "groupid": "2",
                "name": "Linux servers",
                "internal": "0",
                "flags": "0",
                "hosts": [
                    {
                        "hostid": "10318",
                        "host": "Zabbix server"
                    },
                    {
                        "hostid": "10319",
                        "host": "Zabbix agent_1"
                    },
                    {
                        "hostid": "10321",
                        "host": "test"
                    }
                ]
            }
        ],
        "code": 200,
        "msg": "success"
    }
------------------------------
### 接口描述
    删除主机组
#### HTTP方法: 
    DELETE
#### 请求URL: 
    [ip]:8000/v1/hostgroup

#### 请求参数
    {"name": "linux_service"}
#### 返回示例
    {
        "data": {
            "groupids": [
                "16"
            ]
        },
        "code": 200,
        "msg": "success"
    }
-----------------------------------------
### 接口描述
    修改主机组
#### HTTP方法: 
    PUT
#### 请求URL: 
    [ip]:8000/v1/hostgroup

#### 请求参数
    {	
        "name": "test1",
        "groupid": 16
    }
#### 返回示例
    {
        "data": {
            "groupids": [
                "16"
            ]
        },
        "code": 200,
        "msg": "success"
    }
---------------------------------------------------
### 接口描述
    删除主机组
#### HTTP方法: 
    DELETE
#### 请求URL: 
    [ip]:8000/v1/hostgroup

#### 请求参数
    {	
        "groupid": 16
    }
#### 返回示例
    {
        "data": {
            "groupids": [
                "16"
            ]
        },
        "code": 200,
        "msg": "success"
    }