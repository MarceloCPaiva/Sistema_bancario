def criar_usuario(usuarios):
    """
    Cria um novo usuário e o armazena na lista de usuários.
    Argumentos:
    - usuarios: Lista contendo os usuários cadastrados.
    Retorna:
    - usuarios: Lista atualizada com o novo usuário, se criado com sucesso.
    """
    # Solicita as informações do novo usuário ao usuário
    print("Por favor, informe os dados do novo usuário: \n")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento(formato dd/mm/aaaa): ")
    cpf = input("CPF (apenas números sem pontos e traço): ")
    endereco = input("Endereço (formato logradouro, número - bairro - cidade/estado): ")

    # Verifica se o CPF já está cadastrado
    cpf_existente = any(usuario['cpf'] == cpf for usuario in usuarios)
    if cpf_existente:
        print("Erro: Este CPF já está cadastrado.")
        return usuarios
    
    # Adiciona o novo usuário à lista de usuários
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

    return usuarios

def criar_conta_corrente(contas_correntes, usuarios):
    """
    Cria uma nova conta corrente para um usuário existente.
    Argumentos:
    - contas_correntes: Lista contendo as contas correntes cadastradas.
    - usuarios: Lista contendo os usuários cadastrados.
    Retorna:
    - contas_correntes: Lista atualizada com a nova conta corrente, se criada com sucesso.
    """

    # Gera o número da conta corrente sequencial
    numero_conta = len(contas_correntes) + 1

    # Define o número da agência fixo
    numero_agencia = "0001"

    # Solicita o CPF do titular da conta corrente
    cpf = input("Informe o CPF do titular da conta corrente (apenas números): ")

    # Busca o usuário com o CPF informado
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    # Verifica se o usuário foi encontrado
    if not usuario:
        print("Erro: Usuário não encontrado.")
        return contas_correntes
    
    # Cria a nova conta corrente
    nova_conta_corrente = {
        'agencia': numero_agencia,
        'numero_conta': numero_conta,
        'usuario': usuario,
        'saldo': 0,
        'extrato': []
    }

    # Adiciona a nova conta corrente à lista de contas correntes
    contas_correntes.append(nova_conta_corrente)
    print("Conta corrente criada com sucesso!")
    print(f"Número da conta: {numero_conta}")
    print(f"Número da agência: {numero_agencia}")

    return contas_correntes

def realizar_deposito(saldo, valor, extrato):
    """
    Realiza um depósito na conta corrente.
    Argumentos:
    - saldo: Saldo atual da conta corrente.
    - valor: Valor a ser depositado.
    - extrato: Lista contendo o extrato de transações da conta corrente.
    Retorna:
    - saldo: Saldo atualizado após o depósito.
    - extrato: Extrato atualizado com a transação de depósito.
    """

    # Verifica se o valor do depósito é positivo
    if valor <= 0 :
        print("Erro: O valor do depósito deve ser maior do que zero.")
        return saldo, extrato
    
    # Atualiza o saldo da conta corrente
    saldo += valor

    # Adiciona a transação de depósito ao extrato
    extrato.append(f'Depósito: R$ {valor:.2f}')

    print(f'Depósito de R$ {valor:.2f} realizado com sucesso!\n')
    print(f'Saldo atual: R$ {saldo:.2f}.\n')
    print('----------------------------------------------------------------------------------')

    return saldo, extrato

def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque na conta corrente.
    Argumentos:
    - saldo: Saldo atual da conta corrente.
    - valor: Valor a ser sacado.
    - extrato: Lista contendo o extrato de transações da conta corrente.
    - limite: Limite máximo permitido para saque.
    - numero_saques: Número de saques já realizados.
    - limite_saques: Limite máximo de saques permitidos.
    Retorna:
    - saldo: Saldo atualizado após o saque.
    - extrato: Extrato atualizado com a transação de saque.
    """

    # Verifica se o limite de saques foi atingido
    if numero_saques >= limite_saques:
        print(f'Limite de saques atingido. Você já realizou {limite_saques} saques.\n')
        return saldo, extrato, numero_saques
    
    # Verifica se há saldo suficiente para o saque
    if saldo < valor:
        print(f'Seu saldo é: R${saldo:.2f}. Saldo insuficiente para realizar o saque.\n')
        return saldo, extrato, numero_saques
    
    # Atualiza o saldo da conta corrente
    saldo -= valor

    # Adiciona a transação de saque ao extrato
    extrato.append(f'Saque: R${valor:.2f}')

    # Atualiza o número de saques realizados
    numero_saques += 1

    print(f'Saque de R$ {valor:.2f} realizado com sucesso.\n')
    print(f'Saldo atual: R$ {saldo:.2f} \n')
    print('----------------------------------------------------------------------------------')

    return saldo, extrato, numero_saques

def gerar_extrato(saldo, *, extrato):
    """
    Gera o extrato de transações da conta corrente.
    Argumentos:
    - saldo: Saldo atual da conta corrente.
    - extrato: Lista contendo o extrato de transações da conta corrente.
    Retorna:
    - None
    """

    print('Extrato:')
    if not extrato:
        print("Não foram realizadas movimentações.\n")
    else:
        for transacao in extrato:
            print(transacao)
        print(f'Saldo atual: R${saldo:.2f}.\n')
        print('------------------------------------------------------------------------------')

def main():
    depositos_realizados = []
    saques_realizados = []
    saldo = 0
    num_saques = 0
    usuarios = []  # Lista para armazenar os usuários cadastrados
    contas_correntes = []  # Lista para armazenar as contas correntes cadastradas

    while True:

        mensagem = f'''
            ---- Bem vindo ao sistema Bancário! ----

            Para criar um 'usuário', digite: 1
            Para criar uma 'conta corrente', digite: 2
            Para realizar um 'depósito' digite: 3
            Para realizar um 'saque' digite: 4
            Para visualizar o 'extrato' digite: 5
            Para sair do sistema digite: 6

            '''

        print(mensagem)

        opcao = input('Escolha uma opção: ')

        # Criar Usuário
        if opcao == '1':
            usuarios = criar_usuario(usuarios)

        # Criar Conta corrente
        elif opcao == '2':
            contas_correntes = criar_conta_corrente(contas_correntes, usuarios)

        # Realizar um depósito
        elif opcao == '3':
            if not contas_correntes:
                print("Erro: Não há contas correntes cadastradas.")
            else:
                numero_conta = float(input("Informe o número da conta corrente: "))
                conta_corrente = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
                if not conta_corrente:
                    print("Erro: Conta corrente não encontrada.")
                else:
                    valor_deposito = float(input("Informe o valor do depósito: "))
                    conta_corrente['saldo'], conta_corrente['extrato'] = realizar_deposito(conta_corrente['saldo'], valor_deposito, conta_corrente['extrato'])

        # Realizar um saque
        elif opcao == '4':
            if not contas_correntes:
                print("Erro: Não há contas correntes cadastradas.")
            else:
                numero_conta = float(input("Informe o número da conta corrente: "))
                conta_corrente = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
                if not conta_corrente:
                    print("Erro: Conta corrente não encontrada.")
                else:
                    valor_saque = float(input("Informe o valor do saque: "))
                    saldo_anterior = conta_corrente['saldo']
                    conta_corrente['saldo'], conta_corrente['extrato'], conta_corrente['numero_saques'] = realizar_saque(
                        saldo=conta_corrente['saldo'],
                        valor=valor_saque,
                        extrato=conta_corrente['extrato'],
                        limite=500.0,
                        numero_saques=conta_corrente.get('numero_saques', 0),
                        limite_saques=3
                    )
                    if conta_corrente['saldo'] != saldo_anterior:
                        print("Saque realizado com sucesso!")
                        

        # Visualizar o extrato
        elif opcao == '5':
            if not contas_correntes:
                print("Erro: Não há contas correntes cadastradas.")
            else:
                numero_conta = int(input("Informe o número da conta corrente: "))
                conta_corrente = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
                if not conta_corrente:
                    print("Erro: Conta corrente não encontrada.")
                else:
                    gerar_extrato(conta_corrente['saldo'], extrato=conta_corrente['extrato'])

            

        elif opcao == '6':
            print('Saindo...')
            break

        else:
            print('Opção inválida. Tente novamente.\n')
            print('--------------------------------------------------------------------------')

if __name__== "__main__":
    main()