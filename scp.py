#!/usr/bin/env python3
from os import system

def limpiar():
    system("clear")

#limpiar()

print("1.Key")
print("2.passwd")
print("¿Como quieres realizar la conexión?")
metodo = input()

print("Introduce la ruta del archivo a copiar")
origen = input()

print("¿Que usuario se va a conectar?")
usuario = input()

print("¿Cual es la ip del servidor remoto?")
ip = input()

print("¿Que puerto desea usar?")
port = input()

print("¿Cual es la ruta de destino?")
destino = input()

if (metodo=="1"):
    print("¿Donde tienes tu clave privada?")
    key = input()
    system(f"scp -i {key} -p{port} {origen} {usuario}@{ip}:{destino}")

elif (metodo=="2"):
    password = "bolson"
    system(f"sshpass -p{password} scp -p{port} {origen} {usuario}@{ip}:{destino}")

#Script terminado