#!/usr/local/bin/python3
import requests

r = requests.get('https://www.google.com/search', params="{'q': 'doot + doot'}")
d = requests.post('https://www.httpbin.org', params={'item1': 'doot', 'item2': 'doot'})
#r = requests.get('https://www.google.com/search'?q=doot+doot)
#r =requests.get('https://www.google.com/search?source=hp&ei=QjlrW-fLCc_6sAWekLGQDg&q=doot+doot&oq=doot+doot&gs_l=psy-ab.3..0l2j0i20i264k1j0j0i20i264k1j0l5.377.1760.0.2028.10.9.0.0.0.0.97.754.9.9.0....0...1.1.64.psy-ab..1.9.754.0..35i39k1j0i131k1j0i67k1j0i131i67k1j0i131i20i264k1j0i20i263k1j0i10k1.0.eAw12kYglEg')
print(r.url)
print(r.text)


