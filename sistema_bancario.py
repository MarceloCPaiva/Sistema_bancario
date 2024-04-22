depositos_realizados = []
saques_realizados = []
saldo = 0
num_saques = 0

while True:

    mensagem = f'''
    ---- Bem vindo ao sistema Bancário! ----

    Para 'depósito' digite: 1
    Para 'saque' digite: 2
    Para 'extrato' digite: 3
    Para sair do sistema digite: 4

    '''

    print(mensagem)

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            depositos_realizados.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.\n')
            print(f'Saldo atual: R$ {saldo:.2f} \n')
            print(
                '-----------------------------------------------------------------------')
        else:
            print('Valor inválido. O depósito deve ser maior que zero.\n')
            print(
                '-----------------------------------------------------------------------')

    elif opcao == '2':
        if (num_saques < 3):
            valor = float(input('Informe o valor do saque: '))
            if valor > 0 and valor <= 500:
                if saldo >= valor:
                    saldo -= valor
                    saques_realizados.append(valor)
                    num_saques += 1
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.\n')
                    print(f'Saldo atual: R$ {saldo:.2f} \n')
                    print(
                        '------------------------------------------------------------------')
                else:
                    print(f'Seu saldo é: R$ {
                        saldo:.2f}. Saldo insuficiente para realizar o saque.\n')
                    print(
                        '------------------------------------------------------------------')

            else:
                print(
                    'Valor inválido. O saque deve ser maior que zero e no máximo R$ 500.00.\n')
                print(
                    '----------------------------------------------------------------------')
        else:
            print('Limite de saques atingido. Você já realizou 3 saques.\n')
            print(
                '------------------------------------------------------------------')

    elif opcao == '3':
        print('Extrato:')
        if not depositos_realizados and not saques_realizados:
            print('Não foram realizadas movimentações.\n')
            print(
                '----------------------------------------------------------------------')
        else:
            for deposito in depositos_realizados:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in saques_realizados:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {saldo:.2f} \n')
            print(
                '----------------------------------------------------------------------')

    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente.\n')
        print('--------------------------------------------------------------------------')
