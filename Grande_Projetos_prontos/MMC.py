listNM = []  #nome
tamanho = []  #altura
listPS = []  #peso
listMMC = []  #massa corporal
#apaga

# class BreakLoop(Exception):
#     pass

# def minha_funcao():
#     # Ações da função
#     print("Função chamada. Interrompendo o loop.")
#     raise BreakLoop


def addpeso():
    confirm = "S"  #escrever mais 1 ? s ou n
    while confirm.upper() == "S":
        while True:
            try:
                nome = input("digite seu nome ")
                listNM.append(nome.upper())
                #uper faz que mesmo em maisculo ou minisculo funcione
                peso = float(input("digite seu peso "))
                listPS.append(peso)
                altura = float(
                    input("Digite sua altura (EXEMPLO 1,70): ").replace(',', '.'))
                tamanho.append(altura)
                mmc = round(peso / altura**2)
                listMMC.append(mmc)

                break
            except ValueError:
                print("foi feito alguma besteira refaça oq foi feito")
        confirm = input("quer cadastrar mais alguem? (S para continuar)")


# LISTAAAAAAA
def visualizarlista():  #VISUALIZA OS ALUNOS
    if not listNM:
        print("=================== lista vazia =========================")
    else:
        for i in range(len(listNM)):
            #{1:5.2f} | {2:5.2f} | {3:5.2f} serve para dar espaço contado e |
            print("")
            print(' Nome {0} | Peso {1:5.2f} | Tamanho {2:5.2f} | MMC {3:5.2f}'.format(
                listNM[i].ljust(10), listPS[i], tamanho[i], listMMC[i]))


def pesquisar():
    visualizarlista()
    while True:
        apaga = input(
            "qual nome quer pesquisar? (enter sai da tela de list)? ")
        if apaga == '':
            return
        if apaga in listNM:
            i = listNM.index(apaga.upper())
            break
        else:
            print("não existe", apaga)

    print('{0} | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(
    listNM[i].ljust(10), listPS[i], tamanho[i], listMMC[i]))


def allaluno():  #excluir
    visualizarlista()
    while True:
        apaga = input("quem deseja apagar? (enter sai da tela de list) ")
        if apaga == '':
            return
        if apaga.upper() in listNM:
            i = listNM.index(apaga.upper())
            print(i)
            break
        else:
            print("nao existe")

    print('{0} ==> EXCLUIDO | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(
        listNM[i].ljust(10), listPS[i], tamanho[i], listMMC[i]))

    del (listNM[i])
    del (listPS[i])
    del (tamanho[i])
    del (listMMC[i])


#==================== MENU =============+
#não mudar
def menu():  #print da tela inicial
    print("1 - finalizar tudo")
    print("2 - add nome, peso e altura")
    print("3 - Excluir alguem da lista")
    print("4 - mostra lista")
    print("5 - pesquisar aluno")


while True:  #loop
    menu()
    quebrouloop = -1
    while quebrouloop <= 1 or quebrouloop >= 6:
        try:
            quebrouloop = int(input("qual Opção?"))
            break
        except ValueError:
            print("digite sua opção")
    if quebrouloop == 1:
        break
    elif quebrouloop == 2:
        addpeso()
    elif quebrouloop == 3:
        allaluno()
    elif quebrouloop == 4:
        visualizarlista()
    elif quebrouloop == 5:
        pesquisar()
    else:
        print("Deu errado")
print
    #print("escreva de 1 a 4 ples, este numero não pode", quebrouloop)
'''Faça um programa que  cadastra os nomes dos alunos,seu peso e altura em três listas. 
ALUNOS, PESOS,  ALTURAS e IMCs
faça um menu:
1-cadastra alunos pesos e alturas
2-lista todos alunos,   pesos,  altura e imc
3-busca um aluno e seu peso e altura e mostra o  IMC
4-calcula as média da turma de peso,  altura  e  imc
5-fim

Obs: calculo IMC = round(Peso / altura ** 2, 2)
'''
