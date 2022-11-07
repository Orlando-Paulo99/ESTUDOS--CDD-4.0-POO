from biblioteca import ContaBancaria

p1 = ContaBancaria(31241841,'Samuel Lima','Corrente')

print(f'Olá {p1.nome},Bem Vindo ao Banco Do Brasil, o número da sua conta bancária é {p1.numero},sua conta é do tipo {p1.tipo}, seu limite é {p1.limite} R$'

f', e seu saldo é {p1.saldo}R$')

p1.ativar_conta()

p1.depositar(1000)

p1.depositar(100)

p1.saldo=10000

p1.verificar_saldo()

p1.ativarlimite(2000)

p1.sacar(150)






