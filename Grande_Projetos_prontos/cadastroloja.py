

Produtos = ['Cafe', 'Manga'] #declarando as listas
Preco = [2.20, 10] #declarando as listas
Quanti = [10, 20] #declarando as listas
Vendas = [] #declarando as listas
QuantiVendida = [] #declarando as listas

def visualizar():
    print("Produtos:")
    for i in range(len(Produtos)):
        print(f"{Produtos[i]} - Preço: {Preco[i]} - Quantidade: {Quanti[i]}")

def IncluirProdutos():
    confirm = "S"
    while confirm.upper() == "S":
        try:
            produto = input("Nome do seu produto: ")
            preco = float(input("Preço do produto: "))
            quanti = int(input("Quantidade do produto: "))

            Produtos.append(produto)
            Preco.append(preco)
            Quanti.append(quanti)

            confirm = input("Deseja incluir outro produto? (S/N): ")
        except ValueError:
            print("Escreva algo que faça sentido para este tipo de pergunta")

def IncluirVendas():
    visualizar()
    try:
        produto = input("Nome do produto vendido: ")
        if produto in Produtos:
            index = Produtos.index(produto)  # Encontra o índice do produto na lista Produtos
            quantidade_vendida = int(input("Quantidade vendida: "))
            if Quanti[index] >= quantidade_vendida:  # Verifica se há quantidade suficiente no estoque
                Quanti[index] -= quantidade_vendida  # Subtrai a quantidade vendida do estoque
                Vendas.append(produto)  
                QuantiVendida.append(quantidade_vendida)  
                print(f"Venda de {quantidade_vendida} {produto}(s) registrada com sucesso!")
            else:
                print("Quantidade em estoque insuficiente")
        else:
            print("Produto não encontrado")
    except ValueError:
        print("Escreva algo que faça sentido para este tipo de pergunta")

def estoque():
    visualizar()

def vendas():
    print("Relatório de Vendas:")
    for i in range(len(Vendas)):
        # Calcula o valor total da venda multiplicando a quantidade vendida pelo preço do produto
        valor_total = QuantiVendida[i] * Preco[Produtos.index(Vendas[i])]
        print(f"{Vendas[i]} - Quantidade Vendida: {QuantiVendida[i]} - Valor Total: {valor_total:.2f}")

def maisVendas():
    if Vendas:
         # max(set(Vendas), key=Vendas.count) faz o seguinte:
        # - set(Vendas): Cria um conjunto único de produtos vendidos, eliminando duplicatas.
        # - Vendas.count: Conta quantas vezes cada produto aparece na lista Vendas.
        # - max: Encontra o produto que aparece mais vezes (o mais vendido).
        # Encontra o produto mais vendido contando as ocorrências na lista Vendas
        produto_mais_vendido = max(set(Vendas), key=Vendas.count)
        print(f"O produto mais vendido é {produto_mais_vendido} com {Vendas.count(produto_mais_vendido)} vendas")
    else:
        print("Nenhuma venda registrada")

def MediaVendas():
    if QuantiVendida:
        media = sum(QuantiVendida) / len(QuantiVendida)
        print(f"A média de vendas é {media:.2f} produtos por venda")
    else:
        print("Nenhuma venda registrada")

while True:
    try:
        print("*" * 30, " MENU ", "*" * 30)
        print('     1) Incluir novo Produto')
        print('     2) Incluir nova Venda ')
        print('     3) Estoque de produtos e quantidade deles')
        print('     4) Relatório de vendas (histórico de vendas)')
        print('     5) Produtos mais vendidos')
        print('     6) Média de vendas da empresa')
        print('     7) Sair do programa')
        menu = int(input('Digite a opção desejada: '))

        if menu == 7:
            break
        elif menu == 1:
            IncluirProdutos()
        elif menu == 2:
            IncluirVendas()
        elif menu == 3:
            estoque()
        elif menu == 4:
            vendas()
        elif menu == 5:
            maisVendas()
        elif menu == 6:
            MediaVendas()
        else:
            print("Opção inválida")
    except ValueError:
        print('Opção inválida')  # Caso o usuário digite uma opção inválida, o programa irá mostrar essa mensagem