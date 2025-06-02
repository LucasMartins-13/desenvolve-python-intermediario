from datetime import datetime
class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True
        return self.is_concluido

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(titulo, data_hora, descricao):
        return isinstance(titulo, str) and isinstance(data_hora, datetime) and isinstance(descricao, str)

e = Evento("Evento antigo", datetime(2023, 1, 1, 12), "Já aconteceu")
print("Concluído?", e.isConcluido())
print("Eventos criados:", Evento.num_eventos())
print("Válido?", Evento.valida_evento("Oi", datetime.now(), "Desc"))
print("Inválido?", Evento.valida_evento("Oi", "hoje", 123))