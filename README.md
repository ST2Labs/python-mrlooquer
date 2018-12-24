# python-looquer: Python library for Mrlooquer

MrLooquers is an IPv6 Intelligence search engine. And this is a python library for accessing IPV6 Search Engine.

## Features

Implement the RESTFull API for Mr Looquers. Method implement:

    * Query search in whole IPv6 database.

Search Params:

    * query
    * page
    * token 

Raise HTTP Error:

    * 400: QuotedExceeded: dayly quote is exceeded
    * 403: TokenNotValid: the token is not valid

## Instalation

To install the python-mrlooquer library, simply:

    pip install requests

Make git clone, and run

    Don't forget get API-Key by singing up into mrlooquer.com
    Configure API Toke-Key & query into test.py file and run it

## Output example

JSON output example:

    {u'numPages': 106521, u'hits': [
    {u'domain': u'warenpool.com', u'protocol': u'tcp', u'countrycode': u'DE', u'ip': u'2a01:238:20a:202:1066::', u'longitude': 10.5, u'fld': u'warenpool', u'latitude': 51.5, u'timestamp': 1462718604000L, u'ip4': u'81.169.145.66', u'tld': u'com', u'date': u'05/08/16-15:43', u'rdomain': u'w02.rzone.de', u'subdomain': u'', u'banner': u'HTTP/1.1 200 OK\nDate: Sun, 08 May 2016 14:43:23 GMT\nServer: Apache/2.2.31 (Unix)\nLast-Modified: Thu, 30 Sep 2010 09:24:15 GMT\nETag: "470a-3de-49176a4450dc0"\nAccept-Ranges: bytes\nContent-Length: 990\nConnection: close\nContent-Type: text/html\n', u'port': 80}, ... ],
    'total': 1065201, u'max_score': None, u'page': 1}

## Credits
```
    by @rhodius  

www.seguridadparatodos.es
```
## 
