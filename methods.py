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
    tem_arroba = "@" in email
    tem_ptocom = ".com" in email

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

