import calculadora
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
          [ 2 ] subtrair
          [ 3 ] multiplicar
          [ 4 ] dividir
          [ 5 ] sair do menu''')
    opcao = int(input('>>> Qual a opcao desejada? '))
    if opcao == 1:
        print(calculadora.somar(1, 2))
    elif opcao == 2:
        print(calculadora.subtrair(1, 2))
    elif opcao ==3:
        print(calculadora.multiplicar(1, 2))
    else:
        print('Opcao invalida. Tente novamente.')
    print('===' * 10)
print('Fim.')