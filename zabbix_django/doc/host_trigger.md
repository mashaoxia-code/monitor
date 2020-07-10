### 接口描述
    获取主机应用下告警项
#### HTTP方法: GET

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/trigger


#### 请求参数
    无
    
#### 返回示例
    {
        "data": [
            {
                "triggerid": "16780",
                "expression": "{19668}/{19669}>{$LOAD_AVG_PER_CPU.MAX.WARN}\r\nand {19670}>0\r\nand {19671}>0",
                "description": "Load average is too high (per CPU load over {$LOAD_AVG_PER_CPU.MAX.WARN} for 5m)",
                "url": "",
                "status": "0",
                "value": "0",
                "priority": "3",
                "lastchange": "1584078802",
                "comments": "Per CPU load average is too high. Your system may be slow to respond.",
                "error": "",
                "templateid": "16563",
                "type": "0",
                "state": "0",
                "flags": "0",
                "recovery_mode": "0",
                "recovery_expression": "",
                "correlation_mode": "0",
                "correlation_tag": "",
                "manual_close": "0",
                "opdata": "Load averages(1m 5m 15m): ({ITEM.LASTVALUE1} {ITEM.LASTVALUE3} {ITEM.LASTVALUE4}), # of CPUs: {ITEM.LASTVALUE2}"
            },
            {
                "triggerid": "16781",
                "expression": "{19672}>{$CPU.UTIL.CRIT}",
                "description": "High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)",
                "url": "",
                "status": "0",
                "value": "0",
                "priority": "2",
                "lastchange": "0",
                "comments": "CPU utilization is too high. The system might be slow to respond.",
                "error": "",
                "templateid": "16031",
                "type": "0",
                "state": "0",
                "flags": "0",
                "recovery_mode": "0",
                "recovery_expression": "",
                "correlation_mode": "0",
                "correlation_tag": "",
                "manual_close": "0",
                "opdata": "Current utilization: {ITEM.LASTVALUE1}"
            }
        ],
        "code": 200,
        "msg": "success"
    }

#### 注：
    严重程度: priority,
        0 - (default) not classified;
        1 - information;
        2 - warning;
        3 - average;
        4 - high;
        5 - disaster.
    名称：description
    表达式: expression
    状态： status
-----------------------------
### 接口描述
    添加主机应用下告警项
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
    修改主机应用下告警项
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
    删除主机应用下告警项
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