import calculadora
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''[ 1 ] somar
          [ 2 ] subtrair
          [ 3 ] multiplicar
          [ 4 ] dividir
          [ 0 ] sair do menu''')
opcao = int(input('>>> Qual a opcao desejada? '))

def menu2(opcao):
        if opcao == 1:
            print(calculadora.somar(n1, n2))
        elif opcao == 2:
            print(calculadora.subtrair(n1, n2))
        elif opcao == 3:
            print(calculadora.multiplicar(n1, n2))
        elif opcao == 4:
            print(calculadora.dividir(n1, n2))
        elif opcao == 0:
             return print('Fim. Voce saiu.')
        else:
            print('Opcao invalida. Tente novamente.')

menu2(opcao)