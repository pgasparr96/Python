from socket import *

s = socket() #IMPORTAR SOCKET
s.connect(("127.0.0.1", 8729)) #PARÂMETROS PARA CONEXÃO COM O SERVIDOR
s.settimeout(10) #TEMPO DE RESPOSTA DO SERVIDOR. CASO NÃO HAJA RESPOSTA, A CONEXÃO É ENCERRADA

msn = input("Digite uma mensagem:")
cvt = str.encode(msn, "UTF-8") #CONVERSÃO DE STRING PARA BYTES
s.send(cvt) #COMANDO DE ENVIO
print(cvt)
print(f"Foi enviado para o servidor: {msn}")
dd = s.recv(4096)
msnret = dd.decode("UTF-8")
print(f"Resposta do servidor: {msnret}")
msn2 = msnret
cvt = str.encode(msn2, "UTF-8")
s.send(cvt)
#print(cvt)
print(f"Foi enviado novamente para o servidor: {msn2}")
dd = s.recv(4096)
msnret3 = dd.decode("UTF-8")
print(f"Resposta do servidor: {msnret3}")
s.close()