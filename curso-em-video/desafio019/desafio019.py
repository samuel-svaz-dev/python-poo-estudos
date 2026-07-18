#Desafio 19: Crie a classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.
from rich import print
from time import sleep


class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pg_atual = 1
        print(f':book: Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.paginas}'
              f' páginas[/] no total. Você está na [yellow]página 1[/]')


    def avancar_pagina(self, lidas):
        cont = 0
        for c in range(lidas):
            self.pg_atual += 1
            cont += 1
            print(f'Pág {self.pg_atual} -> ', end = '')
            sleep(1)
            if self.pg_atual == self.paginas:
                break
        print(f' [blue]Você avançou {cont} páginas e agora está na[/] [yellow]página {self.pg_atual}[/].')
        if self.pg_atual == self.paginas:
            print(f':closed_book: [red]Você chegou ao final do livro {self.titulo}.[/]')



l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(100)