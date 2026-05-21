lista=["marcelonajjar"]

def validar(log):
    val = 0
    for i in lista:
        if log == i:
            val +=1
        else:
            continue
    return val 



while True:
        print("1-Entrar", "\n2-Cadastrar", "\n3-Sair")
        op = int(input("Opcção"))

        if op == 1:
            nome = str(input("digite o seu nome: "))
            senha = str(input("digite sua senha: "))
            login = nome + senha
            if validar(login) >= 1 :
                print("Olá ", nome)
            elif validar(login) ==0:
                print("Cadastre ou arrume a senha")



        elif op == 2:
            nome = str(input("digite o seu nome: "))
            senha = str(input("digite sua senha: "))
            login = nome + senha
            lista.append(login)

        else:
            print("Obrigado:)")
            break
