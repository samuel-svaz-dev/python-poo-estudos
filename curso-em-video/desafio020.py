#Desafio 20: Crie uma classe Gamer, onde possamos cadastrar nome, nick e os jogos favoritos
# de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.

from rich.panel import Panel
from rich import print


class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_fav = []


    def add_favoritos(self, nome_jogo):
        self.jogos_fav.append(nome_jogo)



    def ficha(self):
        formatado = ':video_game:\n'.join(self.jogos_fav)
        mostra = Panel(f'Nome Real: [white on blue]{self.nome}[/]'
                       f'\nJogos Favoritos: '
                       f'\n:video_game: [blue]{formatado}[/]'
                       , title = f'Jogador <{self.nick}>', width = 40)
        print(mostra)



j1 = Gamer('Samuel Vaz', 'Cyb')
j1.add_favoritos('GTA V')
j1.add_favoritos('EAFC 24')
j1.add_favoritos('Tony Hawks Pro Skater II')
j1.ficha()