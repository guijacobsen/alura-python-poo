# conta = {
#     "numero": 10,
#     "titular": "Guilherme",
#     "saldo": 1000,
#     "limite": 5000
# }

# print('conta: ', conta)
# print('conta.saldo: ', conta['saldo'])


def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('Saldo: {}'.format(conta['saldo']))

c1 = cria_conta(1,"guilherme", 10, 100)
c2 = cria_conta(2,"gabriela", 11, 101)

deposita(c1,10)
sacar(c1,20)
extrato(c1)

# print('conta 1: ', c1)
# print('conta 2: ', c2)