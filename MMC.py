listNM = []  #nome
tamanho = []  #altura
listPS = []  #peso
listMMC = []  #massa corporal
listTOTAL = []  #total


def addpeso():
    confirm = "S"  #escrever mais 1 ? s ou n
    while confirm.upper() == "S":
        while True:
            try:
                nome = input("digite seu nome ")
                listNM.append(nome)
                peso = float(input("digite seu peso "))
                listPS.append(peso)
                altura = float(
                input("Digite sua altura (m): ").replace(',', '.'))
                tamanho.append(altura)
                mmc = round(peso / altura**2, 2)
                listMMC.append(mmc)

                registro = {
                    "nome": nome,
                    "peso": peso,
                    "altura": altura,
                    "mmc": mmc
                }

                listTOTAL.append(registro)

                print(listTOTAL)

                break
            except ValueError:
                print("foi feito alguma besteira refaça oq foi feito")
        confirm = input("cadastrar mais 1 ?")


def allaluno():
    print(listTOTAL)
    excluir = int(input("qual gostaria de excluir ?"))
    listTOTAL.pop(excluir)
    print(listTOTAL)


# def Lista():

# def calculo():
# for i in range(len(listNM)):


#não mudar
def menu():  #print da tela inicial
    print("1 - quebrar")
    print("2 - add nome, peso e altura")
    print("3 - Opção")
    print("4 - Opção")


while True:  #loop
    menu()
    quebrouloop = -1
    while quebrouloop <= 1 or quebrouloop >= 5:
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
        break
    else:
        print("Deu errado")
    print("escreva de 1 a 4 ples, este numero não pode", quebrouloop)
'''Faça um programa que  cadastra os nomes dos alunos,seu peso e altura em três listas. ALUNOS, PESOS,  ALTURAS e IMCs
faça um menu:
1-cadastra alunos pesos e alturas
2-lista todos alunos,   pesos,  altura e imc
3-busca um aluno e seu peso e altura e mostra o  IMC
4-calcula as média da turma de peso,  altura  e  imc
5-fim

Obs: calculo IMC = round(Peso / altura ** 2, 2)
'''
