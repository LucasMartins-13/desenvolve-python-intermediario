#### Classe EventoABC
from abc import ABC, abstractmethod

class EventoABC(ABC):
    def __init__(self, titulo, descricao):
        self._titulo = titulo
        self._descricao = descricao

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def isConcluido(self):
        pass