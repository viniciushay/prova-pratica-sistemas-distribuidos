from xmlrpc.server import SimpleXMLRPCServer

def calcular_pagamento(horas, valor_por_hora):
    return horas * valor_por_hora

servidor = SimpleXMLRPCServer(("localhost", 8005))

servidor.register_function(
    calcular_pagamento,
    "calcular_pagamento"
)

print("Servidor RPC aguardando solicitações,,,")

servidor.serve_forever()
