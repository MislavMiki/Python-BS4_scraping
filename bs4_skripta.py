#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import urllib2

url = 'https://koha.ffzg.hr/cgi-bin/koha/opac-search.pl?idx=ti&q=analiza'
page = urllib2.urlopen(url)
#dekodirano = page.decode('utf8')
#kodirano = dekodirano.encode('utf8')
#soup = BeautifulSoup(kodirano)
soup = BeautifulSoup(page)

naslovi = soup.find_all('a', class_='title')

txtfile = open('/home/mislav/Desktop/output.txt', 'w')

for naslov in naslovi:
        tekst_naslova = naslov.text
        txtfile.write(tekst_naslova.encode('UTF-8')+'\n')

txtfile.close()

