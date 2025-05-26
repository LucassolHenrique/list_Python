# Você deverá criar um sistema de locker de entrega de produtos.
# Lógica: O entregador realiza a entrega de um produto escolhendo a opção ENTREGA. 
#               Informa o tamanho do pacote, o apartamento e finaliza a entrega. O sistema envia uma mensagem ao nome do apartamento cadastrado com uma senha gerada aleatóriamente.
#
#.             O morador, ao retirar o produto, informa o apartamento e a senha, o locker "Abre". O morador Finaliza a retirada e o locker é liberado.
#
#.             Em configurações deve existir uma opção de cadastro, onde o usuário irá cadastrar o apartamento e uma senha para utilizar o locker.

from class_obj import *

def menu():
  print("\nMenu:")
  print("1 - Sair do aplicativo")
  print("2 - Realizar Entrega")
  print("3 - Status do Locker")
  print("4 - Status do Apartamento")
  print("5 - Cadastro de novo apartamento, morador e locker")
  print("6 - Retirar produto")


# Menu principal
while True:
  menu()
  entrada = -1
  while entrada <= 1 or entrada >= 7:
      try:
          entrada = int(input("Escolha uma opção: "))
          break
      except ValueError:
          print("Digite uma opção válida.")

  if entrada == 1:
      print("Saindo do aplicativo...")
      break
  elif entrada == 2:
      realizar_entrega()
  elif entrada == 3:
      status_locker()
  elif entrada == 4:
      status_apartamento()
  elif entrada == 5:
      cadastrar_morador()
  elif entrada == 6:
      retirar_produto()
