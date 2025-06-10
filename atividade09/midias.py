#Classe Base
class Midia:
    def exibirInfo(self):
        pass

#SubClasse Livro
class Livro(Midia):
    def __init__(self, titulo, autor, numeroPaginas):
        self.titulo = titulo
        self.autor = autor
        self.numeroPaginas = numeroPaginas
    
    def exibirInfo(self):
        print(f"Livro:{self.titulo}, Autor: {self.autor}, Páginas {self.numeroPaginas}")

#Subclasse filme
class Filme(Midia):
    def __init__(self, titulo, diretor, duracao):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
    
    def exibirInfo(self):
        print(f"Filme: {self.titulo}, Diretor: {self.diretor}, Duração {self.duracao}")

#Subclasse Musica
class Musica(Midia):
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
    
    def exibirInfo(self):
        print(f"Música: {self.titulo}, Artista: {self.artista}, Duração: {self.duracao}")

#Lista de diferentes Mídias
midia = [
    Livro("O Gato Preto", "Edgar Allan Poe", 90),
    Filme("Cruella", "Disney",140),
    Musica("Provider", "Sleep Token", 605)
]

#Polimorfismo
for midias in midia:
    midias.exibirInfo()