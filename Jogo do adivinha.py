import random

num_min = int(input("Qual é o numero minimo.\n"))
num_max = int(input("Qual é o numero maximo.\n"))
qntTentativas = int(input("Qual é a quantidade de tentativas.\n"))

num_certo = random.randint(num_min,num_max)
 
while True:
    chute = int(input(f"Escolha um número entre {num_min} e {num_max}.\n"))

    if chute == num_certo:
        print(f"Número {num_certo} está correto!!\nParabens")
        break
    elif qntTentativas == 0:
        print(f"Acabou a quantidade de tentativas! O número certo era {num_certo}")
        break
    else:
        qntTentativas -= 1
        if chute < num_certo:
            print(f"O número correto é maior que {chute}.")
        else:
            print(f"O número correto é menor que {chute}.")
        print(f"Você ainda tem {qntTentativas} tentativas.")
