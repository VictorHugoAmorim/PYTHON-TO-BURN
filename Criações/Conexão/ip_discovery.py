import socket as s

#Site que deseja descobrir o IP
host = 'google.com'

#Captura o Ip do host desejado
Ip = s.gethostbyname(host)

#Mostra o resultado
print('O IP do Host {host} é: {Ip})
