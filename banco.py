from datetime import datetime


class Conta:
    def __init__(self, nome, idade, cpf, saldo=0):
        #Inicializa uma conta bancária com os dados do cliente.
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__saldo = saldo
        self.__historico = []  # Lista para registrar o histórico de transações

    def extrato(self):
        #Exibe o extrato da conta, incluindo o histórico de transações.
        print(f"\n--- Extrato da conta de {self.__nome} ---")
        if not self.__historico:
            print("Nenhuma transação realizada até o momento.")
        else:
            for transacao in self.__historico:
                print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
        print(f"Saldo atual: R${self.__saldo:.2f}\n")

    def depositar(self, valor):
        #Realiza um depósito na conta, se o valor for válido.
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor
        self.__registrar_transacao('Depósito', valor)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        #Realiza um saque da conta, se houver saldo suficiente.
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.__saldo -= valor
        self.__registrar_transacao('Saque', valor)
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def transferir(self, valor, conta_destino):
        #Realiza uma transferência para outra conta.
        if not isinstance(conta_destino, Conta):
            raise TypeError("A conta de destino deve ser uma instância da classe Conta.")
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar a transferência.")
        
        # Realiza a transferência
        self.sacar(valor)
        conta_destino.depositar(valor)
        print(f"Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.nome}.")

    def __registrar_transacao(self, tipo, valor):
       #Registra uma transação no histórico da conta.
        self.__historico.append({
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tipo': tipo,
            'valor': valor
        })

    # Métodos para acessar os atributos de forma controlada
    @property
    def nome(self):
        #Retorna o nome do titular da conta.
        return self.__nome

    @property
    def idade(self):
        #Retorna a idade do titular da conta.
        return self.__idade

    @property
    def cpf(self):
        #Retorna o CPF do titular da conta.
        return self.__cpf

    @property
    def saldo(self):
        #Retorna o saldo atual da conta.
        return self.__saldo