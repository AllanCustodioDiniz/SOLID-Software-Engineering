    Single Responsibility Principle (SRP): No código sem os princípios SOLID++, a classe CadastroProdutos não está aderindo ao SRP, pois ela é responsável por gerenciar produtos (adicionar, remover, listar) e também por exibir informações específicas dos produtos.

    Open/Closed Principle (OCP): Não há preocupação com o OCP no código sem os princípios SOLID++. Não há flexibilidade para estender o sistema para diferentes tipos de armazenamento ou para adicionar novas funcionalidades sem modificar a classe existente.

    Liskov Substitution Principle (LSP): Não há hierarquia de classes ou polimorfismo no código sem os princípios SOLID++, portanto não há oportunidade de aplicar o LSP.

    Interface Segregation Principle (ISP): Não há interfaces ou segregação de responsabilidades no código sem os princípios SOLID++. A classe Produto tem a responsabilidade de representar um produto e também de ser manipulada pelo CadastroProdutos.

Diferença e vantagens do código com os princípios SOLID++2:

    Código mais flexível e extensível: O código que adere aos princípios SOLID++2 permite uma maior flexibilidade para adicionar novas funcionalidades sem modificar o código existente. Por exemplo, é possível adicionar diferentes tipos de armazenamento no sistema de cadastro de produtos sem alterar a lógica principal.

    Melhor organização e manutenibilidade: A separação de responsabilidades e a aplicação dos princípios SOLID++2 tornam o código mais organizado, fácil de entender e manter. Cada classe tem uma responsabilidade clara e as interfaces facilitam a interação entre diferentes partes do sistema.

    Facilita o teste e a reutilização: O código que segue os princípios SOLID++2 é mais fácil de testar devido à separação de responsabilidades e à modularidade. Além disso, as classes e interfaces bem definidas podem ser reutilizadas em diferentes partes do código ou em projetos futuros.