from threading import * 
from socket import *
import time
#lista_zenit_polar = {'z':'p', 'e':'o', 'n':'l', 'i':'a', 't':'r'}
zenit = 'zenit'
polar = 'polar'
s = socket()
s.bind((("0.0.0.0", 8729)))
s.listen(10) #NUMERO MÁXIMO DE CLIENTES QUE O SERVIDOR PODE ATENDER ANTES DE RECUSAR

def conn_treat(conn, client):
    dd = conn.recv(4096)
    msnret = dd.decode("UTF-8") #CONVERSÃO DE STRING PARA BYTES
    print(f"String enviada pelo cliente: {msnret}")
    result = cripto_convertor(msnret)
    print(f"Resultado da criptografia: {result}")
    result = str.encode("Enviado:" + result, "UTF=8")
    conn.send(result)
    time.sleep(10)

def cripto_convertor(msncvt):
    global zenit, polar
    text = ''
    x = 0
    for i in range(len(msncvt)):
        msncvt = msncvt.lower()
        z = msncvt[x]
        if z in zenit:
            z = int(zenit.find(msncvt[x]))
            text = text + polar[z]
        elif z in polar:
            z = int(polar.find(msncvt[x]))
            text = text + zenit[z]
        else:
            text = text + msncvt[x]
        x = x + 1
    return text 
    

print("Server online.......")
while True:
    (conn, client) = s.accept()
    Thread (target = conn_treat, args=(conn, client)).start()
'''
while True:
    (conn, client) = s.accept()
    Thread (target = conn_treat, args=(conn, client)).start()
'''

'''
CRIPTOGRAFIA:
zenit, polar = 'zenit', 'polar'
texto = ''
mensagem = input(f"Digite a mensagem:")
n = 0
for i in range(len(mensagem)):
    x = mensagem[n]
    if x in zenit:
        x = int(zenit.find(mensagem[n]))
        texto += polar[x]
    elif x in polar:
        x = int(polar.find(mensagem[n]))
        texto += zenit[x]
    else:
        texto += mensagem[n]
    n += 1

print(texto)
'''
