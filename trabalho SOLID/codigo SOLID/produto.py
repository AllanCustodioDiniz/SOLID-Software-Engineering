class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} - {self.descricao}"

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, descricao, peso):
        super().__init__(nome, preco, descricao)
        self.peso = peso

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, descricao, tamanho_mb):
        super().__init__(nome, preco, descricao)
        self.tamanho_mb = tamanho_mb
