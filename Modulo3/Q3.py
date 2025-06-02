import datetime
class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

    def __str__(self):
        return f"{self.titulo} - {self.data_hora} - {self.descricao} - {self.is_concluido}"

    def __eq__(self, outro): return self.data_hora == outro.data_hora
    def __ne__(self, outro): return self.data_hora != outro.data_hora
    def __lt__(self, outro): return self.data_hora < outro.data_hora
    def __le__(self, outro): return self.data_hora <= outro.data_hora
    def __gt__(self, outro): return self.data_hora > outro.data_hora
    def __ge__(self, outro): return self.data_hora >= outro.data_hora

a = Evento("A", datetime(2025, 6, 1), "Evento A")
b = Evento("B", datetime(2025, 6, 5), "Evento B")

print(a)
print(b)
print("a == b?", a == b)
print("a < b?", a < b)
print("a > b?", a > b)
