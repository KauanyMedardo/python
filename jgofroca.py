print("**************************")
print("bem vindo ao jogo da forca")
print("**************************")

palavra_secreta = "melancia"

enforcou = False
acertou  = False

while(not enforcou and not acertou ):
    
    chute = input("qual a letra?")
    chute = chute.strip( )

    index =0

    for letra in palavra_secreta:
        if (chute ==letra ):
            print (f"encontrei a letra{letra }na posição {index}")
        index = index + 1
    print ("jogando....")
print("fim de jogo")