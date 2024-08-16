
alunos=['GABRIEL', 'LUCAS','RODRIGO', 'JÚLIA','SCHEILA','CAMILA' ]
notas=[7,5,8.7,9,9,8.5]
def mostrarListas():
    print()
    print('#' * 30, ' Lista Turma ', '#' * 30, )
    for i in range(len(alunos)):
        print(f'Aluno: {alunos[i]}  tem nota = {notas[i]}')
        #  print('aluno:', alunos[i],' tem nota ', notas[i])
    print('#' * 50)
def insercao():
    print('#' * 30, ' Insere alunos ', '#' * 30, )
    # rotinaa de inserção
    while True:
        nome = input('Digite o nome do(a) aluno(a):')
        if nome:
            # while TRUE (21) repete enquanto houver erro de digitação
            while True:
                # tratamento de erro
                try:
                    nota = float(input(f'Digite nota de {nome}: '))
                    break  # força saída do while quando Digitação OK
                except:  # Mensagem do erro (aviso para o usuário)
                    print('CRIATURA digite números reais')
            alunos.append(nome.upper())
            notas.append(nota)
        else:
            break  # encerra while linha 11

def calcularMedia():
    print('#' * 30, ' Calcula Média ', '#' * 30)
    mostrarListas()
    media=sum(notas) / len(notas)
    print (f'Media da turma = {round(media,2)}')
    print('#' * 60 )
def buscaAlunoNome():
    print('#' * 30, ' Busca aluno ', '#' * 30)
    mostrarListas()
    while True:
        try:
            nome=input('Digite nome para buscar aluno:')
            indice=alunos.index(nome.upper())
            break
        except:
            print(f'{nome} não está na turma!')
    print(f' {alunos[indice]} tem nota {notas[indice]}')
    print('#' * 60 )




#inicio do Programa
while True: # While repetição do Menu
    print('Escolha uma opção do Menu')
    print('   1) Mostrar conteúdo das listas')
    print('   2) Adicionar nas listas')
    print('   3) Calcular Média da turma')
    print('    4) Busca aluno por nome')
    print('   5) Encerra programa')
    while True: # While Tratamento de Erro
        try:
            opcao=int(input('Opção: '))
            break # Quebra While Tratamento de Erro
        except:
            print('Digite opção valores inteiros [1-5]')
    if opcao==5:
        break # Quebra While repetição do Menu
    elif opcao==1:
        mostrarListas()
        input('Enter => Continua')
    elif opcao==2:
        insercao()
    elif opcao==3:
        calcularMedia()
        input('Enter => Continua')
    elif opcao==4:
        buscaAlunoNome()





print ('fim')

'''Faça um programa que  cadastra os nomes dos alunos,seu peso e altura em três listas. ALUNOS, PESOS,  ALTURAS e IMCs
faça um menu:
1-cadastra alunos pesos e alturas
2-lista todos alunos,   pesos,  altura e imc
3-busca um aluno e seu peso e altura e mostra o  IMC
4-calcula as média da turma de peso,  altura  e  imc
5-fim

Obs: calculo IMC = round(Peso / altura ** 2, 2)
'''