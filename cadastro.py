while True:
    nome = str (input ("digite seu nome completo:"))
    print(f"Seja bem vindo {nome}")
    endereco = str (input(" digite seu endreço:"))
    cpf = float (input ("CPF Ou RG:"))
    numero = float (input("numero de telefone:"))
    print (f"seja bem vinda {nome} seu endereço é {endereco} seu cpf é {cpf} o seu numero é? {numero} ")
    dados= str (input ("vocẽ confirma seus dados?"))
    if dados == "sim":
        input("cadastro finaizado!")
        break
    else:
        input ("vamos refazer o cadastro. Por favor, insira os dados novamente.")

