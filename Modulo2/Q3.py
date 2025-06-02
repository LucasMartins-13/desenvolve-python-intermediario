#### Classe EventoUnico

class EventoUnico(EventoABC):
    def __init__(self, titulo, descricao, data_hora_str):
        super().__init__(titulo, descricao)
        self._data_hora = DataHora()
        self._data_hora.data_hora = data_hora_str

    def isConcluido(self):
        return self._data_hora.isPassado()

    def __str__(self):
        return (f"Evento: {self._titulo}, Data: {self._data_hora.data_hora}, "
                f"Descrição: {self._descricao}, Concluido: {self.isConcluido()}")

    def editar_data_hora(self, nova_data_str):
        self._data_hora.data_hora = nova_data_str
