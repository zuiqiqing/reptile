from BeautifulSoup import BeautifulSoup
import re
f = open("douban.htm", 'r')
buf = f.read()
f.close()
coding = 'utf-8'
soup = BeautifulSoup(buf, fromEncoding=coding)
#found = soup.find(attrs={"title"})
#print soup.html.head.title
found = soup.findAll(text=re.compile('<head>.*?<title>.*?</title>'))
#print found

found = re.search('<tr><td><a\s+?href=\"(?P<hh>.*?)\">.*?</a></td></tr>', buf)
print found.group('hh')