print('Lanches Paladar\n')

print('1. Cadastrar lanchonete')
print('2. Listar lanchonete')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: \n'))
print(f'Você escolheu a opção {opcao_escolhida}\n')

if opcao_escolhida == 1:
    print('Cadastrar lanchonete')
elif opcao_escolhida == 2:
    print('Listar lanchonete')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')