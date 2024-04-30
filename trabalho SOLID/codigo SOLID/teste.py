# Criando uma instância de CadastroProdutos
cadastro = CadastroProdutos()

# Adicionando produtos
produto1 = Produto("Camiseta", 29.99, "Camiseta de algodão")
produto2 = Produto("Calça Jeans", 59.99, "Calça jeans skinny")
cadastro.adicionar_produto(produto1)
cadastro.adicionar_produto(produto2)

# Listando produtos
cadastro.listar_produtos()

# Removendo um produto
cadastro.remover_produto(produto1)

# Listando produtos novamente
cadastro.listar_produtos()
