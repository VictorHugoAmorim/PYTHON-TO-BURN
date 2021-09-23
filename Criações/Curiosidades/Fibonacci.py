qtd = int(input('quantos numeros da sequencia?'))
n1 = 0
n2 = 1
total =3

#print('{}→{}'.format(n1,n2),end='')

while total <= qtd:
    n3 = n1+n2
    print('→ {} '.format(n3),end='')
    n1=n2
    n2=n3
    total +=1
print('fim')
