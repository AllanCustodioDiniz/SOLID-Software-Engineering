from cadastro_produtos import CadastroProdutos
from cadastro_produtos.armazenamento.armazenamento_memoria import ArmazenamentoMemoria
from cadastro_produtos.produto import Produto, ProdutoFisico, ProdutoDigital

# Criação de instâncias
armazenamento = ArmazenamentoMemoria()
cadastro = CadastroProdutos(armazenamento)

# Criar produtos físicos e digitais
produto_fisico = ProdutoFisico("Camiseta", 29.99, "Camiseta de algodão", 0.3)
produto_digital = ProdutoDigital("Ebook", 19.99, "Ebook de romance", 10)

# Adicionar produtos ao cadastro
cadastro.adicionar_produto(produto_fisico)
cadastro.adicionar_produto(produto_digital)

# Listar produtos cadastrados
cadastro.listar_produtos()
