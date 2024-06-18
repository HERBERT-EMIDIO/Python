

# MENU
# https://fsymbols.com/

import textwrap  # Importa o módulo textwrap para formatação de texto

print("""
          
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ██████╗░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██║░░██║██║██║░░██║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║░░██║██║██║░░██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ██████╔╝██║╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚═════╝░╚═╝░╚════╝░
          """)

# Função para exibir o menu e capturar a opção do usuário

def menu():
    # Define o menu como uma string multilinha
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    # Retorna a opção escolhida pelo usuário, removendo a indentação do menu
    return input(textwrap.dedent(menu))

# Função para realizar um depósito
def depositar(saldo, valor, extrato):
    # Verifica se o valor do depósito é positivo
    if valor > 0:
        saldo += valor  # Atualiza o saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona a operação ao extrato
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    # Retorna o saldo e o extrato atualizados
    return saldo, extrato

# Função para realizar um saque
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo
    excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite
    excedeu_saques = numero_saques >= limite_saques  # Verifica se o número de saques excede o limite

    # Verifica as condições para realizar o saque
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor  # Atualiza o saldo
        extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona a operação ao extrato
        numero_saques += 1  # Incrementa o número de saques
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    # Retorna o saldo, extrato e número de saques atualizados
    return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    # Verifica se há movimentações no extrato
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

# Função para criar um novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário já existe

    # Se o usuário já existir, exibe uma mensagem de erro
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    # Solicita as informações do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o novo usuário à lista de usuários
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

# Função para filtrar um usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    # Filtra a lista de usuários para encontrar o usuário com o CPF fornecido
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # Retorna o usuário encontrado ou None se não encontrar
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    # Se o usuário existir, cria a conta
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

# Função para listar todas as contas
def listar_contas(contas):
    # Itera sobre a lista de contas e exibe as informações de cada conta
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

# Função principal do programa
def main():
    LIMITE_SAQUES = 3  # Define o limite de saques diários
    AGENCIA = "0001"  # Define a agência padrão

    saldo = 0  # Saldo inicial
    limite = 500  # Limite de saque
    extrato = ""  # Extrato inicial
    numero_saques = 0  # Número inicial de saques
    usuarios = []  # Lista inicial de usuários
    contas = []  # Lista inicial de contas

    # Loop principal para exibir o menu e capturar as opções do usuário
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executa a função principal
main()



