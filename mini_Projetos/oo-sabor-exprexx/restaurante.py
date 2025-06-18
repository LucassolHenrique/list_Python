
class Restaurante: 
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False       #

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italian pizza')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))