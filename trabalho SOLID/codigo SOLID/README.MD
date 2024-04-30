Cadastro de Produtos em Python

Este é um projeto de cadastro de produtos em Python, desenvolvido como exemplo de aplicação dos princípios SOLID++. Ele consiste em um sistema simples para cadastrar, remover, listar e salvar produtos, aplicando conceitos como Single Responsibility Principle (SRP), Open/Closed Principle (OCP), Liskov Substitution Principle (LSP) e Interface Segregation Principle (ISP).
Funcionalidades

    Cadastro de Produtos: Permite cadastrar produtos informando nome, preço e descrição.
    Remoção de Produtos: Permite remover produtos do sistema.
    Listagem de Produtos: Lista todos os produtos cadastrados.
    Salvamento de Produtos: Salva os produtos cadastrados em um sistema de armazenamento (em memória, arquivo ou banco de dados).

Princípios SOLID++2

    SRP (Single Responsibility Principle): A classe Produto é responsável por representar um produto, enquanto a classe CadastroProdutos é responsável pelo gerenciamento dos produtos.
    OCP (Open/Closed Principle): O sistema suporta diferentes tipos de armazenamento (em memória, arquivo, banco de dados) sem precisar modificar a lógica principal.
    LSP (Liskov Substitution Principle): Subclasses de Produto como ProdutoFisico e ProdutoDigital podem ser usadas de forma intercambiável com a classe base Produto.
    ISP (Interface Segregation Principle): Interfaces como Armazenamento permitem que diferentes implementações de armazenamento tenham apenas os métodos necessários.

Utilização

    Crie uma instância de CadastroProdutos, informando o tipo de armazenamento desejado (em memória, arquivo, banco de dados).
    Adicione produtos utilizando o método adicionar_produto(produto).
    Liste produtos cadastrados utilizando o método listar_produtos().
    Remova produtos utilizando o método remover_produto(produto).
    Salve os produtos utilizando o método salvar_produtos().

    Exemplo de uso:

    from cadastro_produtos import CadastroProdutos, ArmazenamentoMemoria, Produto, ProdutoFisico, ProdutoDigital

# Criar instância de CadastroProdutos com armazenamento em memória
armazenamento_memoria = ArmazenamentoMemoria()
cadastro = CadastroProdutos(armazenamento_memoria)

# Criar produtos
produto1 = Produto("Camiseta", 29.99, "Camiseta de algodão")
produto2 = ProdutoFisico("Livro", 39.99, "Livro de ficção", 0.5)
produto3 = ProdutoDigital("Ebook", 19.99, "Ebook de romance", 10)

# Adicionar produtos
cadastro.adicionar_produto(produto1)
cadastro.adicionar_produto(produto2)
cadastro.adicionar_produto(produto3)

# Listar produtos
cadastro.listar_produtos()

# Remover produto
cadastro.remover_produto(produto1)

# Listar produtos novamente
cadastro.listar_produtos()

# Salvar produtos
cadastro.salvar_produtos()
