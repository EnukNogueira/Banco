# Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python. Ele permite realizar operações básicas em uma conta bancária, como depósitos, saques, transferências e exibição do extrato.

## Funcionalidades

- **Depósito:** Adicione dinheiro à conta.
- **Saque:** Retire dinheiro da conta, respeitando o saldo disponível.
- **Transferência:** Transfira dinheiro entre contas.
- **Extrato:** Visualize o histórico de transações e o saldo atual.

## Como usar

1. Certifique-se de ter o Python instalado em seu computador.
2. Execute o arquivo `banco.py` em um ambiente Python para interagir com as funcionalidades da classe `Conta`.

## Tecnologias Utilizadas

- Python 3.10+
- Biblioteca `datetime` para manipulação de datas.

# Exemplo de uso da classe Conta
from banco import Conta

# Criando contas
conta1 = Conta("Enuk", 30, "123.456.789-00", 1000)
conta2 = Conta("Maria", 25, "987.654.321-00", 500)

# Realizando operações
conta1.depositar(200)
conta1.sacar(100)
conta1.transferir(300, conta2)

# Exibindo extratos
conta1.extrato()
conta2.extrato()

## Autor

Desenvolvido por Enuk como parte de um curso de Python da Danki Code.


