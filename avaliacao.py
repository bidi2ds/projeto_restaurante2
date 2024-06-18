class Avaliacao:
    def _init_(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

    def _str_(self):
        return f"Avaliação: {self.nota} - Comentário: {self.comentario}"