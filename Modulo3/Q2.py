import datetime

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

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(titulo, data_hora, descricao):
        return isinstance(titulo, str) and isinstance(data_hora, datetime) and isinstance(descricao, str)

e = Evento("Antigo", datetime(2023, 1, 1), "Já foi")
e.isConcluido()
print("Concluído:", e.is_concluido)

print("Total:", Evento.num_eventos())
print("Válido:", Evento.valida_evento("Oi", datetime.now(), "Texto"))
print("Inválido:", Evento.valida_evento("Oi", "data errada", 123))
