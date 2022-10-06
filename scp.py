#!/usr/bin/env python3
#scp -i rutakeyprivada ruta origen usuario@ip:/ruta/destino
from os import system


def limpiar():
    system("clear")

#limpiar()

print("1.Key")
print("2.passwd")
#metodo = input("¿Como quieres realizar la conexión?")
print("¿Como quieres realizar la conexión?")
metodo = input()

#limpiar()

#origen = input("Introduce la ruta del archivo a copiar")
#system("clear")

print("Introduce la ruta del archivo a copiar")
origen = input()
#limpiar()

#usuario = input("¿Que usuario se va a conectar?")
print("¿Que usuario se va a conectar?")
usuario = input()
#limpiar()

#ip = input("¿Cual es la ip del servidor remoto?")
print("¿Cual es la ip del servidor remoto?")
ip = input()
#limpiar()

#port = input("¿Que puerto desea usar?")
print("¿Que puerto desea usar?")
port = input()
#limpiar()

#destino = input("¿Cual es la ruta de destino?")
print("¿Cual es la ruta de destino?")
destino = input()
#limpiar()

if (metodo=="1"):
    #key = input("¿Donde tienes tu clave privada?")
    print("¿Donde tienes tu clave privada?")
    key = input()
    system(f"scp -i {key} -p{port} {origen} {usuario}@{ip}:{destino}")

elif (metodo=="2"):
    password = input("introduce la contraseña")
    system(f"sshpass -p{password} scp -p{port} {origen} {usuario}@{ip}:{destino}")
