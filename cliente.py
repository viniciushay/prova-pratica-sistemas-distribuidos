from xmlrpc.client import ServerProxy

servidor = ServerProxy("http://localhost:8005/")

resultado = servidor.calcular_pagamento(8,25)

print("Valor do pagamento:", resultado)
