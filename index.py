napolitanaM = 20.00
margheritaM = 20.00
calabresaM = 25.00
toscanaM = 30.00
portuguesM = 30.00
soma = 0

print('Bem-Vindo a pizzaria do Renan Portela Jorge')
print('----------------------Cardápio---------------------\n'
      '| Código | Descrição  | Pizza Média | Pizza Grande |\n'
      '|   21   | Napolitana |    R$ 20,00 |     R$ 26,00 |\n'
      '|   22   | Margherita |    R$ 20,00 |     R$ 26,00 |\n'  # Cardápio
      '|   23   | Calabresa  |    R$ 25,00 |     R$ 32,50 |\n'
      '|   24   | Toscana    |    R$ 30,00 |     R$ 39,00 |\n'
      '|   25   | Portuguesa |    R$ 30,00 |     R$ 39,00 |\n'
      '---------------------------------------------------')

while True:
    tamanho = input('Informe o tamanho da pizza (M ou G): ')    # Entrada do tamanho
    if tamanho == 'm' or tamanho == 'g':    # Verifica se o tamanho é válido
        codigo = int(input('Informe o código do produto desejado: '))   # Entrada do código
        if codigo < 21 and codigo > 25:    # Verifica se o código é válido
            print('Opção Inválida')
            continue
        else:   # As entradas válidas vão se encaixar em alguma das opções abaixo.
            if tamanho == 'm' and codigo == 21:
                total = napolitanaM
            elif tamanho == 'g' and codigo == 21:
                total = napolitanaM + (napolitanaM * 30 / 100)  # Acrescenta 30% ao valor da pizza média
            elif tamanho == 'm' and codigo == 22:
                total = margheritaM
            elif tamanho == 'g' and codigo == 22:
                total = margheritaM + (margheritaM * 30 / 100)  # Acrescenta 30% ao valor da pizza média
            elif tamanho == 'm' and codigo == 23:
                total = calabresaM
            elif tamanho == 'g' and codigo == 23:
                total = calabresaM + (calabresaM * 30 / 100)  # Acrescenta 30% ao valor da pizza média
            elif tamanho == 'm' and codigo == 24:
                total = toscanaM
            elif tamanho == 'g' and codigo == 24:
                total = toscanaM + (toscanaM * 30 / 100)  # Acrescenta 30% ao valor da pizza média
            elif tamanho == 'm' and codigo == 25:
                total = portuguesM
            elif tamanho == 'g' and codigo == 25:
                total = portuguesM + (portuguesM * 30 / 100)  # Acrescenta 30% ao valor da pizza média
            else:
                print('Opção Inválida.')
                continue
        soma = soma + total
        print('Valor atual R$ {:.2f}\n'.format(soma))  # Mostra valor atual da compra

        algo_mais = int(input('Deseja pedir mais alguma pizza ?\n1 - Sim \n0 - Não '))
        if algo_mais == 1:  # Essa opção permite que o cliente adicione um novo item ao pedido
            continue

        elif algo_mais == 0:
            print('Total a pagar R$ {:.2f}'.format(soma)) # O zero finaliza a compra e mostra o valor total
            soma = soma + total
            break
        else:
            print('Opção Inválida.')  # Mensagem apresentada caso a opção seja inválida
            continue

    else:  # Se o tamanho for inválido este ELSE roda o código do início
        print('Opção Inválida')
        continue