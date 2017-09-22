verdadeiro = True
falso = False
aqui = 1

print(type(verdadeiro), type(falso))
print(verdadeiro)
print(falso)

if aqui <= 1 and 'abacaxi' == 'uva':
    print('\ndoido')
elif aqui <= 2 or 'abacaxi' == 'uva':
    print('\nnem tao doido')
else:
    print('\ncaciudis')

print('\n\nmenu:\n1 - doido\n2 - muito doido\n3 - joão viadinho')

opcao = input('escolha uma opção: ') #tudo que vem aqui é string

if opcao == '1':
    print('\ndoido')
elif opcao == '2':
    print('\nmuito doido')
elif opcao == '3':
    print('\njoão viadinho')
else:
    print('\ndigite uma opção válida por obséquio')