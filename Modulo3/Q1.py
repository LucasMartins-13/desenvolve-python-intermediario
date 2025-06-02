from datetime import datetime
class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

e1 = Evento("Aula", datetime(2025, 6, 2, 10), "Aula de Python")
e2 = Evento("Prova", datetime(2025, 6, 10, 9), "Prova final")

print(vars(e1))
print(vars(e2))
print("Total:", Evento.total_eventos)
