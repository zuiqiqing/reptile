#coding=utf-8

import re
import urllib2,urllib
import hashlib
import cookielib
from BeautifulSoup import BeautifulSoup

filename = 'hdu.html'
loginUrl = 'http://www.douban.com/accounts/login?redir=http://www.douban.com/doumail/'

cookie = cookielib.CookieJar()
openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
'''
md5 = hashlib.md5()
md5.update('87561516')
'''

postdata = urllib.urlencode({
	'source':'None',
	'redir':'http://www.douban.com/doumail/',
	'form_email':'qym9527@foxmail.com',
	'form_password':'7561516',
		})

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

#print postdata

req = urllib2.Request(url=loginUrl, data=postdata, headers=headers)
result = openner.open(req)
#print result.read()
page = result.read()
'''
f = open('xx.htm', 'w')
f.write(page)
f.close()
f = open('xx.htm', 'r')
buf = f.read()
f.close()
print buf
'''
#myPage = re.search('<tr><td><a\s+?href=".*?">我的豆瓣</a></td></tr>' ,result.read().decode('utf-8'))
#myPage = re.findall('<tr><td>.*?', result.read())
found = re.search('<tr><td><a\s+?href=\"(?P<hh>.*?)\">.*?</a></td></tr>', page)
print found.group('hh')

mypageurl = found.group('hh')
rep = openner.open(mypageurl)
print rep.read()