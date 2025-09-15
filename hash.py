import string

statussenha = False
statusemail = False

def validaremail (email):
    tem_arroba = "@" in (email)
    tem_ptocom = ".com" in (email)

    if tem_arroba and tem_ptocom:
        return True
    else:
        return False

def validarsenha (senha):
    tem_tamanho = len(senha) >= 8
    tem_maiuscula = any(caract in string.ascii_uppercase for caract in senha)
    tem_minuscula = any(caract in string.ascii_lowercase for caract in senha)
    tem_numero = any(caract in string.digits for caract in senha)
    tem_especial = any(caract in string.punctuation for caract in senha)

    if tem_tamanho and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return True
    else:
        return False

while not statusemail:
    ogemail = input(
        "Digite seu e-mail para registro: ")

    if validaremail(ogemail):
        print("E-mail registrado com sucesso!")
        statusemail = True
    else:
        print("E-mail inválido! Insira um email válido!")
        statusemail = False

while not statussenha:
    ogsenha = input(
        "Digite a sua senha abaixo.Ela deve ter 8 caracteres alfanuméricos, misturando letras maiúsculas e minúsculas e pelo menos 1 caracter especial.\n Inserir senha:")

    if validarsenha(ogsenha):
        print("HASH da senha registrado!")
        statussenha = True
    else:
        print("Senha inválida! Verifique os requisitos.")
        statussenha = False
