#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os,sys

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'


os.system("clear")

def banner():
	print("""
\033[1;31m░█▀▀▄ ░█▄─░█ ░█▀▀▀█ \033[1;37m\033[1;37m── ▀█▀ ░█▄─░█ ░█▀▀▀ ░█▀▀▀█ \033[0m
\033[1;31m░█─░█ ░█░█░█ ─▀▀▀▄▄ \033[1;37m▀▀ ░█─ ░█░█░█ ░█▀▀▀ ░█──░█ \033[0m
\033[1;31m░█▄▄▀ ░█──▀█ ░█▄▄▄█ \033[1;37m── ▄█▄ ░█──▀█ ░█─── ░█▄▄▄█\033[0m

	         \033[1;41;37m.:R3LI4NT:.\033[0m                                         
""")


def menu():
	print("""
 \033[1;31m[1]\033[0m Consultas DNS
 \033[1;31m[2]\033[0m Whois
 \033[1;31m[3]\033[0m Fuerza Bruta contra dominios
 \033[1;31m[4]\033[0m Reverse IP Lookup
""")