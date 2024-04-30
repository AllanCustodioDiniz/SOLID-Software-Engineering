from abc import ABC, abstractmethod

class Armazenamento(ABC):
    @abstractmethod
    def salvar(self, produtos):
        pass

class ArmazenamentoMemoria(Armazenamento):
    def __init__(self):
        self.produtos = []

    def salvar(self, produtos):
        self.produtos.extend(produtos)
