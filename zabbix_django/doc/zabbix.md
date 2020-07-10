# zabbix-docker搭建
## 准备
### 服务器

- 型号: CentOS Linux release 7.6.1810 (Core)
- 内存：4g
- 磁盘: 32g

### docker
- 版本 1.13.1  
    `sudo yum install docker-ce`

## 安装(下载慢请配置阿里云镜像加速)
- 启动一个MySQL服务器实例  
    ```
    docker run --name mysql-server -t \
        -e MYSQL_DATABASE="zabbix" \
        -e MYSQL_USER="zabbix" \
        -e MYSQL_PASSWORD="zabbix_pwd" \
        -e MYSQL_ROOT_PASSWORD="root_pwd" \
        -d mysql:5.7
    ```
- 启动Zabbix Java gateway实例
    ```
    docker run --name zabbix-java-gateway -t \
      -d zabbix/zabbix-java-gateway:latest

    ```
- 启动Zabbix server实例，并关联这个实例到已创建的MySQL服务器实例
    ```
    docker run --name zabbix-server-mysql -t \
      -e DB_SERVER_HOST="mysql-server" \
      -e MYSQL_DATABASE="zabbix" \
      -e MYSQL_USER="zabbix" \
      -e MYSQL_PASSWORD="zabbix_pwd" \
      -e MYSQL_ROOT_PASSWORD="root_pwd" \
      -e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
      --link mysql-server:mysql \
      --link zabbix-java-gateway:zabbix-java-gateway \
      -p 10051:10051 \
      -d zabbix/zabbix-server-mysql:latest
    ```
- 启动Zabbix web 接口，并将它与MySQL服务器实例和Zabbix server实例关联
    ```
    docker run --name zabbix-web-nginx-mysql -t \
      -e DB_SERVER_HOST="mysql-server" \
      -e MYSQL_DATABASE="zabbix" \
      -e MYSQL_USER="zabbix" \
      -e MYSQL_PASSWORD="zabbix_pwd" \
      -e MYSQL_ROOT_PASSWORD="root_pwd" \
      --link mysql-server:mysql \
      --link zabbix-server-mysql:zabbix-server \
      -p 80:80 \
      -d zabbix/zabbix-web-nginx-mysql:latest
    ```

- 安装agent  
    ```
    rpm -Uvh https://repo.zabbix.com/zabbix/4.4/rhel/7/x86_64/zabbix-release-4.4-1.el7.noarch.rpm

    yum clean all

    yum -y install zabbix-agent

    service zabbix-agent start
    ```
---

## 监控web端[http://122.70.157.50:18041/]
- 打开部署所在服务器 [ip]  初始账户密码 Admin/zabbix

## 架构选型
- server-client架构，直接由zabbix server和zabbix agentd之间进行数据交互。适用于网络比较简单，设备比较少的监控环境。



