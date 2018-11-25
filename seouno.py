#Auditoria SEO I

#Imports

import urllib.request as request
import os
import re
import codecs
from urllib.request import urlopen
from bs4 import BeautifulSoup

print('Auditoria a python.org')

#**********Verificar HTTPS***********#

req = request.Request('http://python.org')
resultado = request.urlopen(req)
print('HTTP OR HTTPS', resultado.geturl())

#********Peso de la pagina********
url = "http://python.org"
print("url: ", url)
site = request.urlopen(url)
meta = site.info()
print("Content-length", site.headers['content-length'])

f = open('out.txt',"r",encoding="utf8")
print('File on disk:', len(f.read()))
f.close()

f = open('out.txt', 'wb')
f.write(site.read())
site.close()
f.close()

f = open('out.txt', 'r')
print('File on disk after download: ', len(f.read()))
f.close()

print('os.stat().st_size returns: ', os.stat('out.txt').st_size)

#*************Verificar world wide web (www) *****************

req = request.Request('http://python.org')
res = request.urlopen(req)
print("Verificando si tiene www: ", res.geturl())

#************Verificar si tiene meta descripcion**************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="lxml")
description = soup.find('meta', attrs={'name': 'description'})
print('El tamaño de descripción es: ', len(description.get('content')))
if(len(description.get('content'))) < 154:
    print('La descripcion es menor a 154')

#***************Verificar etiqueta title**************

html = urlopen('http://python.org')
soup = BeautifulSoup(html.read(), features="lxml")
print("El tamaño del title es: ", len(soup.html.head.title.string))
print("El title de python.org dice: ", soup.html.head.title.string)

#*************Palabras claves***************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="lxml")
keywords = soup.find('meta', attrs = {'name' : 'keywords'})
print('keywords: ', keywords.get('content'))
words = keywords.get('content').split()
print(words)
for word in words:
    print(word, len(soup.findAll(text=re.compile(word))))

#***************Alt imagenes**************************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="lxml")
count = 1
for imagen in soup.findAll('img'):
    print('imagen #', count, ":", imagen["src"])
    print("ALT de imagen #", count, ":", imagen.get('alt', 'none'))
    count += 1
