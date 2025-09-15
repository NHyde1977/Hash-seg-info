import string
import os
import sqlite3
import hashlib

def criar_banco():
  os.remove("cadastros.db") if os.path.exists("cadastros.db") else None

  conexao = sqlite3.connect('cadastros.db')

  sql_create = 'create table cadastros '\
  '(email varchar(255) primary key, '\
  'senha varchar(32))'

  cursor = conexao.cursor()
  cursor.execute(sql_create)

  return cursor, conexao


def converter_senha(senha):
  senha_byte = hashlib.md5(senha.encode())
  senha_hash = senha_byte.hexdigest()

  return senha_hash


def inserir_no_banco(cursor, conexao, email, hash):
  sql_insert = 'insert into cadastros values (?, ?)'

  try:
    cursor.execute(sql_insert, (email, hash))
    conexao.commit()
    print("Cadastro feito com sucesso!")

  except sqlite3.IntegrityError:
    print(f"Erro: e-mail já cadastrado.")

  except Exception as e:
    print(f"Ocorreu um erro: {e}")


def consulta_no_banco(cursor, email):
  consultar_email = 'select senha from cadastros where email = ?'
  cursor.execute(consultar_email, (email,))
  dados = cursor.fetchone()

  if dados:
    return dados[0]
  else:
    return False


def validaremail (email):
    tem_arroba = "@" in (email)
    tem_ptocom = ".com" in (email)

    if tem_arroba and tem_ptocom:
        return True
    else:
        return False


def validarsenha (senha):
    tem_tamanho = len(senha) == 8
    tem_maiuscula = any(caract in string.ascii_uppercase for caract in senha)
    tem_minuscula = any(caract in string.ascii_lowercase for caract in senha)
    tem_numero = any(caract in string.digits for caract in senha)
    tem_especial = any(caract in string.punctuation for caract in senha)

    if tem_tamanho and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return True
    else:
        return False


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
                    print("Senha correta")
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