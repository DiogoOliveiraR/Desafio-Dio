class ContaCorrente:
    def __init__(self, titular, numero_conta, cpf):
        self.titular = titular
        self.numero_conta = numero_conta
        self.cpf = cpf  # CPF do titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Valor de depósito inválido. O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor de saque inválido. O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo atual: R${self.saldo:.2f}")

    def consultar_saldo(self):
        return self.saldo

    @staticmethod
    def validar_cpf(cpf):
        """Valida se o CPF contém exatamente 11 dígitos e apenas números"""
        return cpf.isdigit() and len(cpf) == 11


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome, numero_conta, cpf):
        if numero_conta in self.contas:
            print("Erro: Conta já existe.")
        elif not ContaCorrente.validar_cpf(cpf):
            print("Erro: CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
        else:
            nova_conta = ContaCorrente(nome, numero_conta, cpf)
            self.contas[numero_conta] = nova_conta
            print(f"Conta criada com sucesso! Titular: {nome}, Número da conta: {numero_conta}, CPF: {cpf}")

    def buscar_conta(self, numero_conta):
        if numero_conta in self.contas:
            return self.contas[numero_conta]
        else:
            print("Erro: Conta não encontrada.")
            return None

    def transferir(self, numero_conta_origem, numero_conta_destino, valor):
        conta_origem = self.buscar_conta(numero_conta_origem)
        conta_destino = self.buscar_conta(numero_conta_destino)

        if conta_origem and conta_destino:
            if conta_origem.consultar_saldo() >= valor:
                conta_origem.sacar(valor)
                conta_destino.depositar(valor)
                print(f"Transferência de R${valor:.2f} realizada com sucesso.")
            else:
                print("Erro: Saldo insuficiente para transferência.")
        else:
            print("Erro: Transferência falhou devido a contas inválidas.")


class SistemaBancario:
    def __init__(self):
        self.banco = Banco()

    def exibir_menu(self):
        print("\nSelecione uma operação:")
        print("[d] - Depositar")
        print("[s] - Sacar")
        print("[e] - Extrato")
        print("[nc] - Nova Conta")
        print("[lc] - Listar Contas")
        print("[t] - Transferir")
        print("[q] - Sair")

    def obter_valor(self, valor_tipo):
        while True:
            try:
                valor = float(input(f"Digite o valor para {valor_tipo}: R$"))
                if valor > 0:
                    return valor
                else:
                    print("Erro: O valor deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, insira um número válido.")

    def criar_conta(self):
        nome = input("Digite o nome do titular: ")
        numero_conta = input("Digite o número da conta: ")
        cpf = input("Digite o CPF do titular (somente números): ")
        self.banco.criar_conta(nome, numero_conta, cpf)

    def listar_contas(self):
        if self.banco.contas:
            print("\nListando todas as contas:")
            for conta in self.banco.contas.values():
                print(f"Conta {conta.numero_conta} - Titular: {conta.titular} - CPF: {conta.cpf} - Saldo: R${conta.saldo:.2f}")
        else:
            print("Não há contas cadastradas.")

    def operacoes(self):
        while True:
            self.exibir_menu()

            opcao = input("Digite o número da operação desejada: ").lower()

            if opcao == "d":
                numero_conta = input("Digite o número da conta para depósito: ")
                conta = self.banco.buscar_conta(numero_conta)
                if conta:
                    valor = self.obter_valor("depósito")
                    conta.depositar(valor)
            elif opcao == "s":
                numero_conta = input("Digite o número da conta para saque: ")
                conta = self.banco.buscar_conta(numero_conta)
                if conta:
                    valor = self.obter_valor("saque")
                    conta.sacar(valor)
            elif opcao == "e":
                numero_conta = input("Digite o número da conta para extrato: ")
                conta = self.banco.buscar_conta(numero_conta)
                if conta:
                    conta.extrato()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "t":
                numero_conta_origem = input("Digite o número da conta de origem: ")
                numero_conta_destino = input("Digite o número da conta de destino: ")
                valor = self.obter_valor("transferência")
                self.banco.transferir(numero_conta_origem, numero_conta_destino, valor)
            elif opcao == "q":
                print("Saindo... Até logo!")
                break
            else:
                print("Erro: Opção inválida. Tente novamente.")


# Programa principal
if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.operacoes()
