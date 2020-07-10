### 接口描述
    获取主机下应用
#### HTTP方法: GET

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application


#### 请求参数
    无
    
#### 返回示例
    {
    "data": [
        {
            "applicationid": "1334",
            "hostid": "10319",
            "name": "CPU",
            "flags": "0",
            "templateids": [
                "1142"
            ]
        }
    ],
    "code": 200,
    "msg": "success"
}

---------------------------
### 接口描述
    添加主机下应用项
#### HTTP方法: 
    POST

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application


#### 请求参数
    {
        "name":"test"
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
    [ip]:8000/v1/host/[host_id]/application


#### 请求参数
    {
        "name":"test3",
        "applicationid": 1348
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

-----------------------------

### 接口描述
    删除主机下应用项
#### HTTP方法: 
    DELETE

#### 请求URL: 
    [ip]:8000/v1/host/[host_id]/application


#### 请求参数
    {
        "applicationid": 1348
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