while True:
    nome = str(input("digite seu nome completo: "))
    print (f"seja bem vindo {nome}")
    diavencimento= int(input ("dia que sua fatura vai vencer:"))
    mesanovencimento =int(input("mês em que a fatura vai vencer:"))
    valorfatura= int (input ("valor da fatura:"))
    print (f"valor da fatura é {valorfatura} vai vencer no dia {diavencimento} do mês {mesanovencimento}")