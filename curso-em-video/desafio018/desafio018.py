#Desafio 18: Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e
#mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Churrasco:

    def __init__(self, nome, pessoas):
        self.nome = nome
        self.pessoas = pessoas
    
    def analisar(self):
        titulo = self.nome
        carne = self.pessoas * 0.4
        custo_total = carne * 82.4
        custo_pessoa = custo_total / self.pessoas
        painel = Panel(f'Analisando o [green]{self.nome}[/] com [blue]{self.pessoas}[/] convidados \n'
                       'Cada participante comerá 0,4 kg e custa R$82,40 \n'
                       f'Recomendo [blue]comprar {carne}Kg [/] de carne \n'
                       f'O custo total será de [gree]R${custo_total:.2f}[/] \n'
                       f'Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/] para participar',
                       title = titulo, width=70)
        print(painel)



c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()
#Considere:
#Consumo padrão: 400g por pessoa
#Preço carne: R$82,40 / Kg