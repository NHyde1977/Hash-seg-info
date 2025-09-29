from methods import *
if __name__ == '__main__':

    cursor, conexao = criar_banco()

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar (e-mail + senha)")
        print("2 - Validar login (e-mail + senha)")
        print("3 - Pesquisar hash")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Cadastro
            statussenha = False
            statusemail = False

            while not statusemail:
                ogemail = input("Digite seu e-mail para registro: ")
                if validaremail(ogemail):
                    print("E-mail registrado com sucesso!")
                    statusemail = True
                else:
                    print("E-mail inválido! Insira um email válido!")

            while not statussenha:
                ogsenha = input(
                    "Digite a sua senha (APENAS 8 caracteres, maiúsculas, minúsculas, número e especial): "
                )
                if validarsenha(ogsenha):
                    print("HASH da senha registrado!")
                    statussenha = True
                else:
                    print("Senha inválida! Verifique os requisitos.")

            senha_convertida = converter_senha(ogsenha)
            inserir_no_banco(cursor, conexao, ogemail, senha_convertida)

        elif opcao == "2":
            # Validação
            login_email = input("E-mail: ")
            login_senha = input("Senha: ")

            senha_convertida = converter_senha(login_senha)
            consultar = consulta_no_banco(cursor, login_email)

            if consultar:
                if senha_convertida == consultar:
                    print("Conta Válida")
                else:
                    print("Senha incorreta")
            else:
                print("E-mail inexistente")

        elif opcao == "3":
            # Pesquisa hash
            email = input("E-mail: ")
            consultar = consulta_no_banco(cursor, email)

            if consultar:
                print(f"Hash:", consultar)
            else:
                print("E-mail inexistente")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")