#### Classe DataHora
from datetime import datetime, timedelta

class DataHora:
    FORMAT = '%d/%m/%Y, %H:%M'

    def __init__(self):
        self._data_hora = None

    @property
    def data_hora(self):
        return self._data_hora.strftime(self.FORMAT) if self._data_hora else None

    @data_hora.setter
    def data_hora(self, valor):
        try:
            self._data_hora = datetime.strptime(valor, self.FORMAT)
        except ValueError:
            raise ValueError("Formato de data/hora inválido. Use dd/mm/aaaa, hh:mm")

    def isPassado(self):
        return self._data_hora < datetime.now()

    def somaDias(self, num_dias):
        data_hora_somada = self._data_hora + timedelta(days=num_dias)
        return data_hora_somada.strftime(self.FORMAT)