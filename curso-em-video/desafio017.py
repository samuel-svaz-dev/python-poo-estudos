#Desafio 017: Crie a classe Produto, onde podemos cadastrar nome e o preço.
#Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    
    def etiqueta(self):
        linha = '-' * 35
        preco_formatado = f'R${self.preco}'
        mostra = Panel(f'{self.nome} \n {linha} \n {preco_formatado}'.center(60), title = 'Produto', width = 40)
        print(mostra)
    

p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('NoteBook Gamer', 8_000.00)
p2.etiqueta()