#Desafio 017: Crie a classe Produto, onde podemos cadastrar nome e o preço.
#Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    
    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        preco_formatado = f"R${self.preco:.2f}"
        conteudo += f"{preco_formatado.center(30, '.')}"
        card = Panel(conteudo, title = 'Produto', width = 34)
        print(card)
    

p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('NoteBook Gamer', 8_000.00)
p2.etiqueta()