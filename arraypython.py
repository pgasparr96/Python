array = []
for i in range(0,10):
   n = int(input('Informe o valor:'))
   while True:
     if n in array:
       n=int(input('Valor já encontrado no array. Informe outro valor:'))
     else:
       break
   array.append(n)
print(array)
array.sort()
print(array)
print(array[8])
