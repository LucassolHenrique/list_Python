# ## Gerenciamento de Estoque e Vendas em Python

# **Descrição:**

# Este programa em Python auxilia no gerenciamento de estoque e vendas de produtos, utilizando menus interativos para facilitar a navegação. O programa armazena informações em quatro listas:

# * **Produtos:** Armazena os nomes dos produtos cadastrados.
# * **Preços:** Armazena os preços correspondentes a cada produto.
# * **Estoque: ** Armazena a quantidade de estoque em cada produto
# * **Vendas:** Armazena os nomes dos produtos vendidos.
# * **Quantidades:** Armazena as quantidades vendidas de cada produto.

# **Funcionalidades:**

# **Menu:**

# * **Incluir Produto:** Permite adicionar um novo produto à lista de produtos, seu preço à lista de preços e quantidade de estoque.
# * **Incluir Venda:** Permite registrar a venda de um produto, selecionando-o da lista de produtos e informando a quantidade vendida e deve abater da quantidade de estoque.
# * **Relatório de Estoque:** Exibe a lista completa de produtos com seus respectivos preços e quantidades em estoque (quantidades cadastradas - quantidades vendidas).
# * **Relatório de Vendas:** Exibe a lista completa de produtos vendidos com suas respectivas quantidades vendidas e valor total de venda.
# * **Produto Mais Vendido:** Identifica e exibe o produto com maior quantidade vendida.
# * **Média de Vendas:** Calcula e exibe a média de produtos vendidos.
# * **Sair:** Encerra o programa.

# **Observações:**

# * O programa utiliza estruturas de decisão (if/else) e laços de repetição (for/while) para controlar o fluxo do programa e gerenciar as listas de dados.
# * O programa não possui salvamento de dados persistente. As informações nas listas são armazenadas apenas durante a execução do programa.
# * Este programa serve como base para aprimoramentos, como inclusão de funcionalidades para salvar dados em arquivos, gerar relatórios mais detalhados, implementar um sistema de autenticação de usuário, entre outras.

# **Exemplos de Uso:**

# * Cadastrar um novo produto: "mouse" e seu preço: R$ 25,00
# * Registrar a venda de 2 unidades de "mouse"
# * Gerar o relatório de estoque para verificar a quantidade restante de "mouse"
# * Consultar o produto mais vendido e sua quantidade total vendida
# * Calcular a média de produtos vendidos em todas as vendas registradas

# **Este programa é ideal para alunos iniciantes em Python, pois permite praticar conceitos básicos da linguagem, como:**

# * Variáveis e tipos de dados
# * Listas e suas operações
# * Estruturas de controle (if/else, for/while)
# * Funções
# * Entrada e saída de dados

# **Além de auxiliar no aprendizado da linguagem Python, o programa também oferece uma ferramenta prática para gerenciar estoque e vendas de produtos de forma simples e organizada.**

# ## Avaliação de Respostas dos Alunos para o Programa de Gerenciamento de Estoque e Vendas em Python

# **Critérios de Avaliação:**

# **Funcionalidade:**

# * **(40%) Correção das funcionalidades:**
#     * O programa deve implementar todas as funcionalidades descritas no enunciado, incluindo:
#         * Incluir produtos, preços e quantidades de estoque.
#         * Incluir vendas, atualizando o estoque.
#         * Gerar relatórios de estoque e vendas completos e informativos.
#         * Identificar o produto mais vendido e calcular a média de vendas.
#     * O programa deve funcionar de acordo com as regras descritas, como:
#         * Atualizar o estoque corretamente após cada venda.
#         * Exibir informações precisas nos relatórios.
#         * Identificar o produto mais vendido corretamente.

# * **(10%) Usabilidade do Menu:**
#     * O menu deve ser claro, intuitivo e fácil de usar.
#     * As opções do menu devem estar descritas de forma compreensível.
#     * A navegação pelo menu deve ser fluida e sem erros.

# **Código:**

# * **(30%) Qualidade do Código:**
#     * O código deve estar bem escrito, organizado e formatado de acordo com as boas práticas de programação em Python.
#     * Variáveis, funções e estruturas de controle devem ter nomes descritivos e fáceis de entender.
#     * O código deve estar comentado para explicar sua lógica e funcionalidade.

# * **(10%) Eficiência do Código:**
#     * O código deve ser eficiente e otimizado para evitar redundâncias e processamentos desnecessários.
#     * Algoritmos e estruturas de dados devem ser adequados para o problema.
#     * O código deve ser robusto e capaz de lidar com entradas inesperadas.

# **Apresentação:**

# * **(10%) Documentação:**
#     * O programa deve ter uma documentação clara e concisa que explique:
#         * A funcionalidade do programa.
#         * Como usar o programa.
#         * A estrutura do código.

# * **(5%) Criatividade e Originalidade:**
#     * O programa pode apresentar soluções criativas e originais para os problemas de gerenciamento de estoque e vendas.
#     * O aluno pode implementar funcionalidades adicionais que não estão descritas no enunciado, mas que sejam relevantes para o problema.

# **Observações:**

# * A avaliação será feita de forma individualizada, considerando o nível de conhecimento e experiência de cada aluno.
# 
# COMPARATIVO COM O CODIGO QUE EU HAVIA FEITO.
import re
produtos=[]
precos=[]
estoque=[]
vendas=[]
quantidades=[]
lucros=[]
def IncluirProduto():

    while True:
        qnt_produtos=input("quantos produtos voce quer registrar? ")
        if(check_letras(qnt_produtos)==False and check_espaco(qnt_produtos)):
            break
        print("voce digitou um valor invalido!")

    for i in range(0,int(qnt_produtos)):
        
        while True:
            nome_produto = input("Nome do produto: ")
            if(check_letras(nome_produto) and check_espaco(nome_produto)):
                break
            print("voce digitou um valor invalido!")

        while True:
            preco_produto = input("preço do produto: ")
            if(check_letras(preco_produto)==False and check_espaco(preco_produto)):
                preco_produto=float(preco_produto)
                break
            print("voce digitou um valor invalido!")
        
        while True:
            estoque_produto= input("quanto estoque tem: ")
            if(check_letras(estoque_produto)==False and check_espaco(estoque_produto)):
                estoque_produto=int(estoque_produto)
                break
            print("voce digitou um valor invalido!")

        novo_produto = {"nome": nome_produto}
        novo_preco = {nome_produto : preco_produto}
        novo_estoque = {nome_produto : estoque_produto}
        nova_venda = {nome_produto : 0}
        novo_lucro = {nome_produto: 0}
        produtos.append(novo_produto)
        precos.append(novo_preco)
        estoque.append(novo_estoque)
        vendas.append(nova_venda)
        lucros.append(novo_lucro)
        print("\nProduto adicionado:")
        print(f"\nNome: {produtos[i]["nome"]}\nPreço = {precos[i][produtos[i]["nome"]]}\nEstoque = {estoque[i][produtos[i]["nome"]]}\n")

    print("produtos adicionados:")
    for i in range(0,len(produtos)):
        print(f"\nNome: {produtos[i]["nome"]}\nPreço = {precos[i][produtos[i]["nome"]]}\nEstoque = {estoque[i][produtos[i]["nome"]]}")
    hub()

def IncluirVenda():
    Vendas_ids=[]
    for i in range(0,len(produtos)):
        Vendas_ids.append(i+1)
    for i in range(0,len(produtos)):
        print(f"{i+1} - {produtos[i]["nome"]}")
    while True:
        Venda = input('Que produto foi comprado? ')
        if(check_letras(str(Venda))==False and check_espaco(str(Venda)) and str(Venda) in str(Vendas_ids)):
            while True:
                qnt_venda = input("Quantos produtos foram solicitados? ")
                if check_letras(qnt_venda)==False and check_espaco(qnt_venda):
                    if int(qnt_venda) <= estoque[int(Venda)-1][produtos[int(Venda)-1]["nome"]]:
                        qnt_venda=int(qnt_venda)
                        break
                    else:
                        print("Esse valor excede o limite do estoque! ")
                        while True:
                            escolha_estoque=input("Voce quer adicionar mais estoque a este produto?\n1-sim\n2-não\n")
                            escolha_estoque_int= int(escolha_estoque)
                            if (check_letras(escolha_estoque)==False and check_espaco(escolha_estoque) and escolha_estoque_int <3 and escolha_estoque_int >0):
                                if escolha_estoque_int == 1:
                                    AdicionarEstoque(int(Venda)-1)
                                    break
                                elif escolha_estoque_int == 2:
                                    hub()
                            print("voce digitou um valor invalido! ")
                                
                else:
                    print("voce digitou um valor invalido! ")

            break
        print("voce digitou um valor invalido! ")
    print("\n")
    vendas[int(Venda)-1][produtos[int(Venda)-1]["nome"]]+=qnt_venda
    estoque[int(Venda)-1][produtos[int(Venda)-1]["nome"]]-=qnt_venda
    lucros[int(Venda)-1][produtos[int(Venda)-1]["nome"]]+=qnt_venda*precos[int(Venda)-1][produtos[int(Venda)-1]["nome"]]
    hub()
def RelatorioDeEstoque():
    for i in range(len(produtos)):
        print(f"Produto: {produtos[i]["nome"]}\nPreço: R${precos[i][produtos[i]["nome"]]}\nEstoque: {estoque[i][produtos[i]["nome"]]}\n")
    hub()
def RelatorioDeVendas():
    for i in range(len(produtos)):
        lucro=lucros[i][produtos[i]["nome"]]
        print(f"{produtos[i]["nome"]}:\nVendas: {vendas[i][produtos[i]["nome"]]}\nLucro: R${round(lucro,2)}\n")
    hub()
def ProdutoMaisVendido():
    mais=[]
    for i in range(len(produtos)):
        mais.append(vendas[i][produtos[i]["nome"]])
    for i in range(len(produtos)):
        if vendas[i][produtos[i]["nome"]]==max(mais):
            mais_produto=produtos[i]["nome"]
    print(f"O produto mais vendido é {mais_produto} com {max(mais)} vendas")
    hub()

def MediaDeVendas():
    media_vendas=0
    for i in range(len(produtos)):
        media_vendas+=vendas[i][produtos[i]["nome"]]
    media_vendas=media_vendas/len(produtos)
    print(f"A media de vendas é {round(media_vendas,2)}")
    hub()

def AdicionarEstoque(i):
    while True:
        mais_estoque=input("Quanto você que adicionar? ")
        if (check_letras(mais_estoque)==False and check_espaco(mais_estoque)):
            mais_estoque=int(mais_estoque)
            break
        print("voce digitou um valor invalido! ")
    estoque[i][produtos[i]["nome"]]+=mais_estoque

def check_letras(texto):
    return bool(re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', texto))

def check_espaco(texto):
    return not texto.isspace() and texto != ''
def hub():
    opcao=input("qual opção voce quer?\n1 - incluir produto\n2 - incluir venda\n3 - relatorio de estoque\n4 - relatorio de venda\n5 - media de vendas\n6 - produto mais vendido\n7 - sair\n")
    opcao_int= int(opcao)
    if (check_letras(opcao)==False and check_espaco(opcao)):
        if opcao_int == 1:
            IncluirProduto()
        elif opcao_int == 2:
            IncluirVenda()
        elif opcao_int == 3:
            RelatorioDeEstoque()
        elif opcao_int == 4:
            RelatorioDeVendas()
        elif opcao_int == 5:
            MediaDeVendas()
        elif opcao_int == 6:
            ProdutoMaisVendido()
        elif opcao_int == 7:
            exit()
        else:
            print("voce digitou um valor invalido! ")
IncluirProduto()
hub()