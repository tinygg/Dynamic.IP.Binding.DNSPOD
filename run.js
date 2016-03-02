var dnspod = require('dnspod-client');
fs = require('fs');

config = JSON.parse(fs.readFileSync('config.json'));

var Dnspod = require('dnspod-client');

var client = new Dnspod({
        'login_email': config.account.email,
        'login_password': config.account.pwd
    });

// client
//     .domainList({length: 5})
//     .on('domainList', function (err, data) {
//         if (err) {
//             throw err;
//         } else {
//         	console.log(data);
//         }
//     });
function refresh()
{
	client
	    .getHostIp()
	    .on('getHostIp', function (err, ip_addr) {
	        if (err) {
	            throw err;
	        } else {
	            //console.log('get IP address: ' + ip_addr);

	            // 接口地址：

	            //          https://dnsapi.cn/Record.Modify

	            // HTTP请求方式：

	            //         POST

	            // 请求参数：

	            //         公共参数
	            //         domain_id 域名ID，必选
	            //         record_id 记录ID，必选
	            //         sub_domain 主机记录，默认@，如 www，可选
	            //         record_type 记录类型，通过API记录类型获得，大写英文，比如：A，必选
	            //         record_line 记录线路，通过API记录线路获得，中文，比如：默认，必选
	            //         value 记录值, 如 IP:200.200.200.200, CNAME: cname.dnspod.com., MX: mail.dnspod.com.，必选
	            //         mx {1-20} MX优先级, 当记录类型是 MX 时有效，范围1-20, mx记录必选
	            //         ttl {1-604800} TTL，范围1-604800，不同等级域名最小值不同，可选
	            //         status [“enable”, “disable”]，记录状态，默认为”enable”，如果传入”disable”，解析不会生效，也不会验证负载均衡的限制，可选
	            //         weight 权重信息，0到100的整数，可选。仅企业 VIP 域名可用，0 表示关闭，留空或者不传该参数，表示不设置权重信息


	            client.recordModify(
	            	{
	            		domain_id: config.domain.domain_id,
	            		record_id:config.domain.record_id,
	            		sub_domain:config.domain.sub_domain,
	            		record_type:config.domain.record_type,
	            		record_line:config.domain.record_line,
	            		mx:config.domain.mx,
	            		value:ip_addr
	            	})
	                .on('recordModify', function (err, data) {
	                    if (err) {
	                        throw err;
	                    } else {
	                    	console.log(data.status.created_at+ '\t' + data.record.value + '\t' + data.status.message);
	                    }
	                });
	        }
	    });
}


refresh();
setInterval(function() {   refresh();}, +config.interval * 60 * 1000);