##作用

  没有申请外网静态IP的情况下,实现域名动态IP绑定
  
##原理

-  依赖DNSPOD.CN开放接口
-  *获取当前服务器外网IP,比对域名解析的IP地址,不一致则解析为当前的外网IP地址,一致则什么也不做*
    改为:直接获取IP地址,并更新
-  *每次查询都会记录日志*
    改为:用forever自带的log和error日志

##条件

-  有DNSPOD账号并且添加了独立域名
-  路由器做好端口映射
-  *服务器装好python我的版本是2.7*
-  *服务器新建windows计划任务,定期执行2min比较合适*
    改为:node forever后台运行: forever start -l log.txt -e err.txt -o out.txt -a  run.js  
    相关命令：forever list\ forever stop run.js\ forever stopall
-  *任务执行程序和参数:python  path-to-DNSPOD_CN_Login.py*
-  安装node,并安装插件:dnspod-client,forever

##注意

-  *执行频率不能过快,否则IP查询接口服务站点会屏蔽你的请求*
-  记得将config.sample.json改为config.json,对应地修改里面的配置项

## 升级日志 

### 0.1.0 

采用ip138.com接口

### 0.2.0 

- 改成nodejs版本
- 清理项目,采用sublime text编写测试
- 改用配置文件config.json的形式
- 采用dnspod提供的IP获取方法(这才是正确的姿势！！！)
