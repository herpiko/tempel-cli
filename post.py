import urllib
import urllib2

url = 'http://tempel.blankon.in'
values = {'language' : 'bash',
      'content' : 'isi'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 

#print response.read()
print 'URL     :', response.geturl()
