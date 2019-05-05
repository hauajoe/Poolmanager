# Import der Datun aus Bayrol Poolmanager
# Dokumentation unter: http://www.bayrol-poolaccess.de
import xmltodict
import urllib2
req = urllib2.Request("http://192.168.0.10//cgi-bin/webgui.fcgi?xmlitem=34.4001")
opener = urllib2.build_opener()
f = opener.open(req)
doc = xmltodict.parse(f.read())
print (doc['pm5']['item']['@label'] + "  " +  doc['pm5']['item']['@value'].replace('.',','))


req = urllib2.Request("http://192.168.0.10//cgi-bin/webgui.fcgi?xmlitem=34.4022")
opener = urllib2.build_opener()
f = opener.open(req)
doc = xmltodict.parse(f.read())
print (doc['pm5']['item']['@label'] + "  " +  doc['pm5']['item']['@value'])

req = urllib2.Request("http://192.168.0.10//cgi-bin/webgui.fcgi?xmlitem=34.4033")
opener = urllib2.build_opener()
f = opener.open(req)
doc = xmltodict.parse(f.read())
print (doc['pm5']['item']['@label'] + "  " +  doc['pm5']['item']['@value'].replace('.',','))

req = urllib2.Request("http://192.168.0.10//cgi-bin/webgui.fcgi?xmlitem=34.4069")
opener = urllib2.build_opener()
f = opener.open(req)
doc = xmltodict.parse(f.read())
print (doc['pm5']['item']['@label'] + "  " +  doc['pm5']['item']['@value'].replace('.',','))

req = urllib2.Request("http://192.168.0.10//cgi-bin/webgui.fcgi?xmlitem=34.4071")
opener = urllib2.build_opener()
f = opener.open(req)
doc = xmltodict.parse(f.read())
print (doc['pm5']['item']['@label'] + "  " +  doc['pm5']['item']['@value'].replace('.',','))

