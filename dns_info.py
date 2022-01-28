#!/usr/bin/env python
#_*_ coding: utf8 _*_

from banner.banner import *
import dns.resolver
import requests
from bs4 import BeautifulSoup
from os import path
import time 

banner()
menu()

def consultas():
    consultas = ['URL','A','AAAA','SOA','CAA','CNMAE','MX','PTR','SRV','TXT','MF','NS','MD','MB','MINFO','TTL','PTR']
    for c in consultas:
        try:
            a = dns.resolver.resolve(url,c)
            for q in a:
                print(q)

        except:
            print("\033[1;31m[!] \033[0;31mConsulta no encontrada\033[0m") 	


def whois():
    a = requests.get("https://who.is/whois/{}".format(url))
    soup = BeautifulSoup(a.text,'html5lib')
    for l in soup.find_all("pre"):
        print(l.get_text())

def brute_force():
    wordlist = input("\033[1;37mWORDLIST:\033[0m ")
    print("")
    if path.exists(wordlist):
        wordlist = open(wordlist,'r')
        wordlist = wordlist.read().split('\n')
        lista = []
        for s in wordlist:
            try:
                a = dns.resolver.resolve('{}.google.com'.format(s),'A')
                lista.append('{}.{}'.format(s,url))
            except:
                pass
        if len(lista) > 0:
            print('\033[1;32m[+] \033[0;32mNumero de subdominios posibles:\033[0m {}'.format(len(lista)))
            for d in lista:
                print('\033[1;31mFound : \033[0m' + d)               
        else:
            print("\033[1;31m[!] \033[0;31mNo se encontraron dominios\033[0m") 
    else:
        print("\033[1;31m[!] \033[0;31mArchivo no encontrado\033[0m")  

def reverse_ip_lookup():
    agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
    r = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(url),headers=agent)
    b = BeautifulSoup(r.text,'html5lib')
    c = b.find(id="null")
    d = c.find(border="1")
    for l in d.find_all("tr"):
        print("\033[1;31mFound : \033[0m" + l.td.string)


option = int(input("--> "))
url = input("\033[1;31mURL / IP:\033[0m ")


if option == 1:
	consultas()

elif option == 2:
	whois()

elif option == 3:
	brute_force()

elif option == 4:
	print("")
	reverse_ip_lookup()

