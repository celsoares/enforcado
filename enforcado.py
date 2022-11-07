
import random
import os
from datetime import datetime
import time


with open(r"C:\Users\Celso Soares\Desktop\LP\M8\palavras.txt", "r") as file:
    lista_palavras=file.readlines()
    palavra_oculta=random.choice(lista_palavras).strip("\n")

    #print(palavra_oculta)
print("Jogo do enforcado...")
print("A palavra já foi seleccionada ...")
print("Boa sorte! Tens 6 tentativas")

palavra=[]
for x in range(len(palavra_oculta)):
    palavra.append("_")

print(palavra)

er=0
inicio=time.time()
while er<6:
    if "_" not in palavra:
        print("Ganhou!!")
        result="V"
        break

    letra=input("introduza uma letra: ").upper()

    os.system("cls")

    if letra in palavra_oculta:
        for x in range (len(palavra_oculta)):
            if letra==palavra_oculta[x]:
                palavra[x]=letra
        print(palavra)
    else:
        print("Letra não encontrada")
        er+=1
        print("erros=", er)
        print(palavra)

else:
    print("Excedeu o nº de tentativas!! Perdeu!!")
    result="P"
    print("Palavra oculta é: ", palavra_oculta)

temp =round((time.time() - inicio), 1)
print(temp)
temp=str(f"o seu tempo foi de: {temp} segundos")

with open ("resultados.txt", "a", encoding="utf_8") as file:
    
    file.write(datetime.now().strftime("%m/%d/%Y - %H:%M"))
    file.write(f",{result}, {er}, {temp}\n")




#Passo 1 - Abrir o ficheiro palavras.txt modo r
#passo 2 - criar uma lista com todas as palavras do ficheiro (readlines)
#passo 3 - random.choice da lista (para escolher a palavra aleatorimente)
#passo 4 - palavra.strip("\n")


#Passo 1 - Abrir o ficheiro resultados.txt modo a
#passo 2 - write(datatime.now, "V P", tentativas, tempo\n)











