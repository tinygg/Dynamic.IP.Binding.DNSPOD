#coding=utf8
import urllib2
import re
import sys
import ssl
import time
import os
from dnspod.apicn import *

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    email = "your email"
    password = "your password"
    #可以从dnspod后台管理界面，浏览器抓包获取，record id也一样，也可以用发送请求的方式获取json
    domain_id = 'your domain id '
    kxnf_record_id = 'your record id'
    domain_name = 'your sub domain = record'#不是全部比如  A.abc.com 则只需要填A
    
    log_path = 'C:\update_ip_records.txt'
    ##kxnf = 104917035
    ##kxnf1 = 104970653
    
    current_ip = '';#ip地址
    
    need_update = False
    
    #查找IP地址的网站ip138.com
    FindIPUrl = "http://1111.ip138.com/ic.asp";
    
    Header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4'
            }
    '''
    step1.查找IP地址
    '''
    ssl._create_default_https_context = ssl._create_unverified_context
    
    req = urllib2.Request(FindIPUrl, headers=Header)
    content = urllib2.urlopen(req).read();
    
    #print content;
    
    #解析IP
    tempIP = re.findall(r"\[(.*)\]", content);
    if(len(tempIP) > 0):
        current_ip = tempIP[0];
        print current_ip;  
          
    '''
    step2.比较记录
    '''
    print "RecordInfo"
    api = RecordInfo(domain_id=domain_id, record_id = kxnf_record_id, email=email, password=password)
    before_ip = str(api().get("record").get("value"))
    print u'当前设置的IP地址:%s' % before_ip
    if(before_ip != current_ip): 
        need_update = True
        print u'当前IP地址需要更新，正在更新...'
    else:
        need_update = False
        print u'当前IP地址不需要更新'
    '''
    step3.更新记录
    '''
    if os.path.isfile(log_path):
        log = file(log_path,'a')
    else:
        log = file(log_path)
        log = file(log_path,'a')
    if(need_update):
        print "Modify Record"
        api = RecordModify(
                       record_type="A",
                       record_line=u'默认'.encode("utf8"), 
                       sub_domain = domain_name,
                       value=current_ip, 
                       mx=10, 
                       domain_id=domain_id,
                       record_id=kxnf_record_id,
                       email=email, 
                       password=password
                       )
        status = api().get("status",{}).get("message")
        record = api().get("record")
        
        print "update result:", status
        print "Record Newer:", record

        log.write(u'update @'+time.strftime('%Y-%m-%d %X',time.localtime(time.time()))+'\t'
                  + before_ip + '\t -> \t' +record['value'].decode('utf8')+'\r\n')

    else:
        log.write(u'same @'+time.strftime('%Y-%m-%d %X',time.localtime(time.time()))+'\t'
                  + '\r\n')
    log.close()


        
#     domain_id = api().get("domain", {}).get("id")
#     print "%s's id is %s" % (domain, domain_id)
    
'''    
    api = DomainList(email=email, password=password)
    print api().get("domains")
    
    print "RecordList"
    api = RecordList(domain_id=domain_id,email=email, password=password)
    print str(api().get("records"))
    
'''
    
    
if(__name__ == '__main__'):
    main()
    
