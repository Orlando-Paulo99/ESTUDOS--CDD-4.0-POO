#criação da conta bancaria
class ContaBancaria:

    def __init__(self,numero,nome,tipo,limite=0,status=False,saldo=0):
        self.numero = numero
        self.__saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite
    def depositar(self,valor):
        self.saldo = self.saldo + valor
        if self.status == True:

            print(f'Seu Depósito de {valor}R$ foi realizado com sucesso')
        else:
            print('Sua conta está desativada')
    def sacar(self,valor):

        self.saldo = self.saldo - valor

        if self.status == True:
                while True:
                    if valor>self.limite:
                        print("saque maior que o limite")
                        break
                    elif self.saldo+self.limite>valor:
                        print("valor insuficiente")
                        break

                    else:
                        print("saque realizado com sucesso")
                        break

     def ativar_conta(self):
        if self.status == False:
            self.status = True
            print('Sua conta está ativa')
        else:
            print('não pode ativar, a conta ja esta ativa')
     
      def verificar_saldo(self):
        if self.status == True:
            print(f"seu saldo é: {self.saldo}")

        else:
            print("sua conta está desativada ,não é possivel ver o saldo")

      def ativarlimite(self,valor):
        self.limite=valor
        if  self.status==True:
            print(f"seu limite de credito foi aprovado e o valor é {valor} com vencimento dia 30")
        else:
            print("sua conta não foi ativa")














