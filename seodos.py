#Auditoria SEO II

#Imports

import urllib.request as request
import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

print('Auditoria a python.org')

#**********Verificar la cantidad de H1***********#

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features= "lxml")
for h1 in soup.findAll('h1'):
    print('Este es un h1: ', h1)
    print("En total son: ", len(soup.findAll('h1')))

#*****************Enlaces rotos*******************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features= "lxml")
links = []
elements = soup.select('a')

for element in elements:
    link = element.get('href')
    if link.startswith('http'):
        links.append(link)

print(links)

for link in links[:10]:
    petition = urlopen(link)
    print('Enlace: ', link, "Respuesta: ", petition.code)

#*************Existencia del archivo robots.txt y sitemap xml******************

for file in os.listdir(r'C:\Users\lenovo\PycharmProjects\EdteamProject\public_HTML'):
    if(file.endswith(".txt")):
        print("Se encontro el archivo robots.txt en: ", os.path.join(r'C:\Users\lenovo\PycharmProjects\EdteamProject\public_HTML', file))

for file in os.listdir(r'C:\Users\lenovo\PycharmProjects\EdteamProject\public_HTML'):
    if(file.endswith(".xml")):
        print("Se encontro el archivo sitemap.xml en: ", os.path.join(r'C:\Users\lenovo\PycharmProjects\EdteamProject\public_HTML'))

#**************Existencia del Favicon**********

url = "http://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page, features= "lxml")
icon_link = soup.find('link', rel = "icon")
icon = request.urlopen(url + icon_link['href'])
with open("test.ico", "wb") as f:
    try:
        f.write(icon.read())
        print("Succes!")
    except:
        print("No hay icono")

#******************Verificar si el sitio tiene analytics*****************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="lxml")
if(soup.findAll(text=re.compile(".google-analytics"))):
    print("Contiene google analytics")
else:
    print("no contiene analytics")

#******************Verificar el idioma***************

site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features= "lxml")
lang = soup.find('html')['lang']
print('El idioma del sitio web es, lang = ',lang)

#**********Verificar charset utf8***********
site = "http://python.org"
print("pagina: ", site)
peticion = request.urlopen(site)
meta = petition.info()
print(meta) #para ver el contenido del servidor de la pagina
#print()

#********viewport************
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="lxml")
print(soup.find('meta', attrs={'name':'viewport'}))

