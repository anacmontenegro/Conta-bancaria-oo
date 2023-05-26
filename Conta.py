class Conta:
    # ---- CONSTRUTOR ----
    def __init__(self, numero_da_conta, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # ---- GETTERS ----
    @property
    def numero_da_conta(self):
        return self.__numero_da_conta

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # ---- SETTERS ----
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # ---- MÉTODOS ----
    def extrato(self):
        print("Oi, {}! Seu saldo é: R${}. Seu limite é: R${}.".format(self.__titular.title(), self.__saldo, self.__limite))

    # Para descobrir se há fundos suficientes para sacar
    def __para_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque
    
    # Para efetuar o saque
    def sacar(self, valor):
        if (self.__para_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Não é possível sacar esse valor pois ultrapassa o limite.")

    def depositar(self, valor):
        self.__saldo += valor
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        if (self.__para_sacar(valor)):
            print("{}, você transferiu R${} para {}.".format(self.__titular.title(), valor, destino.__titular.title()))
            destino.depositar(valor)
            print("{}, você recebeu um depósito de R${}.".format(destino.__titular.title(), valor))
        else: 
            print("A transferência não pôde ser efetuada.")
