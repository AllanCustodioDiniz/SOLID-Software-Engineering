class CadastroProdutos:
    def __init__(self, armazenamento):
        self.armazenamento = armazenamento
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def salvar_produtos(self):
        self.armazenamento.salvar(self.produtos)
