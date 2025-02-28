while True:
    valorCapital = int(input("digite o valor do seu capital : \n"))
    print("vamos considerar uma selic de 13,25 por cento e ver quanto renderá seu capital.")
    rentabilidadeBruta = valorCapital * 1.1325

    print (f"se vocẽ investir seu dinheiro na selic no fim do ano vocẽ terá :\n {rentabilidadeBruta}")


    faturamneto = int (input("digite o faturamenrro do sue negócio em um ano"))

    lucroliquido = faturamneto * 0.15

    if (lucroliquido < rentabilidadeBruta) :
        print ("o negocio não é viavel ")
        print (f"o seu lucro liquido é {lucroliquido}")
        break
    
    else:
        print("o negocio é viavel ")
        print(f"o seu lucro liquido é {lucroliquido}")
        break