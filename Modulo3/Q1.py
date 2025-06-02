from datetime import datetime

class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

e1 = Evento("Reunião", datetime(2025, 6, 2, 10), "Reunião de equipe")
e2 = Evento("Prova", datetime(2025, 6, 10, 14), "Prova de matemática")

print(e1.titulo, e1.data_hora, e1.descricao, e1.is_concluido)
print(e2.titulo, e2.data_hora, e2.descricao, e2.is_concluido)
print("Total de eventos:", Evento.total_eventos)
