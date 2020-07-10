### 接口描述
    登陆
#### HTTP方法: POST

#### 请求URL: 
    [ip]:8000/login

#### Body请求示例:
    {
    	"username": "zabbix",
    	"password": "admin",
    }
#### 请求参数

|参数|是否必选|类型|描述
|-|-|-|-
|username|是|string	|用户名
|password|是|string|用户密码
    
#### 返回示例
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMCwidXNlcm5hbWUiOiJ6YWJiaXgiLCJleHAiOjE1ODU5NjQwNzUsImVtYWlsIjoiYWRtaW4iLCJvcmlnX2lhdCI6MTU4MzM3MjA3NX0.hngI5TNllznlkt6ajqfB1510RKvoXVK8NsEWl3jKyXk"
    }


