##作用

  没有申请外网静态IP的情况下,实现域名动态IP绑定
  
##说明

-  依赖DNSPOD.CN开放接口
-  node库dnspod-client,获取IP地址,并调用DNSPOD的recordModify更新接口
-  用forever自带的-l,-o,-e记录日志
-  记得将config.sample.json改为config.json,对应地修改里面的配置项

##条件

-  有DNSPOD账号并且添加了独立域名,添加A记录,例如ABC.your-domain.com
-  路由器做好端口映射
-  改为:node forever后台运行: forever start -l log.txt -e err.txt -o out.txt -a  run.js  
   相关命令：forever list\ forever stop run.js\ forever stopall
-  安装node,并安装插件:dnspod-client,forever

## 升级日志 

### 0.1.0 

采用ip138.com接口

### 0.2.0 

- 改成nodejs版本
- 清理项目,采用sublime text编写测试
- 改用配置文件config.json的形式
- 采用dnspod提供的IP获取方法(这才是正确的姿势！！！)
