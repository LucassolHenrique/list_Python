
import random

#foi importado o random 
numero_secreto = random.randrange(1,101) #vai de 1 a 100 (101) é numero que não pode ir 
#numero_secreto = round(random.random() * 100) #pode ir pra a cima de 100 e como zero coisa que não deveria
#numero_secreto = numero aleatorio
total_de_tentativa = 4 #do while 
rodada = 1

#cada tentativa contabiliza -1 até 0
while(rodada <= total_de_tentativa):
    print("tentativa {} de {}".format(rodada, total_de_tentativa))
    chute_str = input("Digite o seu numero entre 1 e 100")
    print("voce digitou", chute_str)
    chute = int(chute_str)
    
    if(chute < 1 and chute > 100):
        print("abaixo de 100 favor")
        
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if(acertou):
        print("Voce Acertou!")
        break
    else:
        if(maior):
                print("Voce Errou! O seu chute foi maior do que o numero secreto")
        if(menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
        rodada = rodada + 1
    #fazendo 99321806 que o codigo diminui o valor de total_de_tentativa ate 0