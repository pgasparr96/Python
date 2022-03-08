'''
OBJETIVO:

O seu objetivo neste exercício é criar um sistema distribuído, seguindo o modelo cliente_servidor, para validação de CPFs. O seu sistema deverá
ser composto por duas partes(uma para o cliente e outra para o servidor) que devem possuir as características e funcionalidades descritas
abaixo.

CLIENTE:

O Cliente deverá solicitar ao usuário diversos CPFs a serem validados. Para cada CPF, o cliente deverá enviar o CPF para o servidor,
receber uma mensagem "VÁLIDO" ou "INVÁLIDO" e avisar o usuário se o CPF é válido ou não. Este procedimento deverá ser repetido até que
o usuário digite um CPF vazio.

SERVIDOR:

O servidor deverá ser implementado prevendo a possibilidade de diversas conexões simultâneas. Para tal, deve utilizar uma thread para 
cada conexão.
Para cada conexão, o servidor deverá receber CPFs a serem validados. Para cada CPF, ele deve verificar se é composto por caracteres 
válidos (números, pontos e traço) e se os dígitos de verificação correspondem ao algoritmo abaixo. Os formatos de entrada válido são:
somente números e o formato XXX.XXX.XXX-XX.
A porta a ser utilizada pela servidor será 8729.

ALGORITMO PARA CÁLCULO DOS DÍGITOS DO CPF:

VALIDAR CPF:

O cálculo do CPF é baseado nos 2 dígitos finais.
Para validar, pegue os nove primeiros dígitos do CPF, gere os dois dígitos e salve em um novo CPF.
Compare se o CPF enviado é igual ao CPF gerado. 
Se verdadeiro, o CPF é válido, caso contrário, inválido. 

*OBTER PRIMEIRO DÍGITO:
1 - Multiplicar os 9 primeiros dígitos do CPF por uma contagem regressiva iniciando de 10 e terminando em 2.
2 - Somar todos os valores das multiplicações do passo 1. 
3 - Obter o resto da divisão entre a soma do passo 2 e 11. 
'''


from socket import *
cpf = '1'
s = socket() #IMPORTAR SOCKET
s.connect(("127.0.0.1", 8729)) #PARÂMETROS PARA CONEXÃO COM O SERVIDOR
s.settimeout(10) #TEMPO DE RESPOSTA DO SERVIDOR. CASO NÃO HAJA RESPOSTA, A CONEXÃO É ENCERRADA

while (cpf != NULL):
    cpf = input("Digite um CPF(com a formatação de números, pontos e traço):")
    msg = str.encode(cpf, "UTF-8")
    s.send(msg)
    print(f"Enviando: {msg}")
    print("**************************")
    dd = s.recv(4096)
    msgret = dd.decode("UTF-8")
    print(f"Resposta do servidor: {msnret}")
print("Programa encerrado...")
s.close()