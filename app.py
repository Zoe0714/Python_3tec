import os

def exibir_nome_do_programa():
    print('Lanches Paladar\n')

def exibir_opcoes()
    print('1. Cadastrar lanchonete')
    print('2. Listar lanchonete')
    print('3. Ativar restaurante')
    print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: \n'))
print(f'Você escolheu a opção {opcao_escolhida}\n')

def finalizar_app():
    os.system('cls')
    print('Finalizar o app')

if opcao_escolhida == 1:
    print('Cadastrar lanchonete')
elif opcao_escolhida == 2:
    print('Listar lanchonete')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()

    if __name__ == '__main__':
        main()