# Função que processa a string do estoque inicial e converte em uma lista de dicionários
def carregar_estoque_inicial(estoque_inicial):
    """
    Carrega o estoque inicial a partir de uma string formatada e transforma em uma lista de dicionários,
    cada um representando um produto..
    
    Retorna uma lista de produtos.
    """
    produtos = estoque_inicial.split("#")
    estoque = []
    for produto in produtos:
        descricao, codigo, quantidade, custo, preco_venda = produto.split(";")
        estoque.append({
            "descricao": descricao,
            "codigo": int(codigo),
            "quantidade": int(quantidade),
            "custo": float(custo),
            "preco_venda": float(preco_venda)
        })
    return estoque


# Função para adicionar novo produto ao estoque
def cadastrar_produto(estoque):
    """
    Pede ao usuário os dados de um novo produto (descrição, código, quantidade, custo, preço de venda)
    e o adiciona à lista de estoque.
    
    Imprime uma mensagem de sucesso após o cadastro.
    """
    descricao = input("Qual a descrição do produto? ")
    codigo = int(input("Qual o código do produto?: "))
    quantidade = int(input("Qual a quantidade do produto?: "))
    custo = float(input("Qual o custo do produto?: "))
    preco_venda = float(input("Qual é o preço de venda do produto?: "))
    
    estoque.append({
        "descricao": descricao,
        "codigo": codigo,
        "quantidade": quantidade,
        "custo": custo,
        "preco_venda": preco_venda
    })
    print("Produto cadastrado com sucesso!")


# Função que lista todos os produtos cadastrados
def listar_produtos(estoque):
    """
    Mostra na tela uma lista de todos os produtos que estão cadastrados no estoque,
    com seus detalhes: descrição, código, quantidade, custo e preço de venda.
    """
    print("\nLista de Produtos:")
    for produto in estoque:
        print(f"Descrição: {produto['descricao']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Custo: {produto['custo']}, Preço de Venda: {produto['preco_venda']}")


# Função para ordenar os produtos por quantidade
def ordenar_produtos_por_quantidade(estoque, ordem="crescente"):
    """
    Ordena os produtos pela quantidade em estoque. A ordem pode ser crescente ou decrescente,
    de acordo com o parâmetro 'ordem'.
    
    Após a ordenação, lista os produtos novamente.
    """
    if ordem == "crescente":
        estoque.sort(key=lambda p: p["quantidade"])
    else:
        estoque.sort(key=lambda p: p["quantidade"], reverse=True)
    listar_produtos(estoque)


# Função para buscar produto por descrição ou código
def buscar_produto(estoque, *, descricao=None, codigo=None):
    """
    Busca um produto no estoque, seja pela descrição ou pelo código. 
    Exibe os detalhes do produto caso encontrado, ou uma mensagem indicando que não foi encontrado.
    """
    if descricao:
        encontrados = [p for p in estoque if descricao.lower() in p["descricao"].lower()]
    elif codigo:
        encontrados = [p for p in estoque if p["codigo"] == codigo]
    
    if encontrados:
        for produto in encontrados:
            print(f"Descrição: {produto['descricao']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Custo: {produto['custo']}, Preço de Venda: {produto['preco_venda']}")
    else:
        print("Produto não encontrado.")


# Função para remover um produto com base no código
def remover_produto(estoque, codigo):
    """
    Remove um produto do estoque com base no código fornecido. 
    Exibe uma mensagem de confirmação ou erro, dependendo se o produto foi encontrado.
    """
    for produto in estoque:
        if produto["codigo"] == codigo:
            estoque.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")


# Função que lista produtos esgotados
def listar_produtos_esgotados(estoque):
    """
    Verifica se há produtos esgotados (com quantidade 0) no estoque
    e exibe a lista dos que se encontram nessa condição.
    """
    esgotados = [p for p in estoque if p["quantidade"] == 0]
    if esgotados:
        print("\nProdutos esgotados:")
        for produto in esgotados:
            print(f"Descrição: {produto['descricao']}, Código: {produto['codigo']}")
    else:
        print("Nenhum produto esgotado.")


# Função que filtra produtos com baixa quantidade
def filtrar_produtos_baixa_quantidade(estoque, limite=5):
    """
    Filtra os produtos que possuem quantidade abaixo do limite definido. 
    Se nenhum limite for informado, o valor padrão é 5.
    """
    baixa_quantidade = [p for p in estoque if p["quantidade"] < limite]
    if baixa_quantidade:
        print("\nProdutos com baixa quantidade:")
        for produto in baixa_quantidade:
            print(f"Descrição: {produto['descricao']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}")
    else:
        print("Nenhum produto com baixa quantidade.")


# Função para atualizar o estoque de um produto
def atualizar_estoque(estoque, codigo, quantidade):
    """
    Atualiza a quantidade de um determinado produto no estoque. A quantidade pode ser aumentada ou diminuída,
    dependendo do valor fornecido (positivo para adicionar, negativo para reduzir).
    """
    for produto in estoque:
        if produto["codigo"] == codigo:
            produto["quantidade"] += quantidade
            print("Estoque atualizado com sucesso!")
            return
    print("Produto não encontrado.")


# Função para atualizar o preço de venda de um produto
def atualizar_preco_venda(estoque, codigo, novo_preco):
    """
    Altera o preço de venda de um produto, desde que o novo preço não seja menor que o custo.
    """
    for produto in estoque:
        if produto["codigo"] == codigo:
            if novo_preco >= produto["custo"]:
                produto["preco_venda"] = novo_preco
                print("Preço de venda atualizado com sucesso!")
            else:
                print("Erro: o novo preço de venda não pode ser menor que o custo.")
            return
    print("Produto não encontrado.")


# Função que calcula o valor total do estoque
def calcular_valor_total_estoque(estoque):
    """
    Calcula o valor total de todos os produtos no estoque, com base na quantidade e no preço de venda.
    """
    total = sum(p["quantidade"] * p["preco_venda"] for p in estoque)
    print(f"Valor total do estoque: R$ {total:.2f}")


# Função que calcula o lucro presumido
def calcular_lucro_presumido(estoque):
    """
    Calcula o lucro presumido, subtraindo o custo do preço de venda e multiplicando pela quantidade de cada produto.
    """
    lucro = sum((p["preco_venda"] - p["custo"]) * p["quantidade"] for p in estoque)
    print(f"Lucro presumido do estoque: R$ {lucro:.2f}")


# Função que gera um relatório geral do estoque
def gerar_relatorio_geral(estoque):
    """
    Gera um relatório completo de todos os produtos no estoque, exibindo detalhes como 
    descrição, código, quantidade, custo, preço de venda e o valor total por produto.
    """
    print("\nRelatório Geral do Estoque:")
    print("Descrição".ljust(30), "Código".ljust(10), "Qtd".rjust(5), "Custo".rjust(10), "Preço Venda".rjust(12), "Total".rjust(12))
    for produto in estoque:
        total_item = produto["quantidade"] * produto["preco_venda"]
        print(f"{produto['descricao'].ljust(30)} {str(produto['codigo']).ljust(10)} {str(produto['quantidade']).rjust(5)} {str(produto['custo']).rjust(10)} {str(produto['preco_venda']).rjust(12)} {str(total_item).rjust(12)}")
    
    calcular_valor_total_estoque(estoque)

# Menu interativo para o usuário
def menu(estoque):
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Ordenar Produtos por Quantidade")
        print("4. Buscar Produto")
        print("5. Remover Produto")
        print("6. Listar Produtos Esgotados")
        print("7. Filtrar Produtos com Baixa Quantidade")
        print("8. Atualizar Estoque")
        print("9. Atualizar Preço de Venda")
        print("10. Calcular Valor Total do Estoque")
        print("11. Calcular Lucro Presumido")
        print("12. Gerar Relatório Geral")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            ordem = input("Digite 'crescente' ou 'decrescente': ")
            ordenar_produtos_por_quantidade(estoque, ordem)
        elif opcao == "4":
            descricao = input("Digite a descrição (ou deixe em branco): ")
            codigo = input("Digite o código (ou deixe em branco): ")
            if descricao:
                buscar_produto(estoque, descricao=descricao)
            elif codigo:
                buscar_produto(estoque, codigo=int(codigo))
        elif opcao == "5":
            codigo = int(input("Digite o código do produto: "))
            remover_produto(estoque, codigo)
        elif opcao == "6":
            listar_produtos_esgotados(estoque)
        elif opcao == "7":
            limite = input("Digite o limite de quantidade (ou deixe em branco para usar o valor padrão 5): ")
            if limite:
                filtrar_produtos_baixa_quantidade(estoque, int(limite))
            else:
                filtrar_produtos_baixa_quantidade(estoque)
        elif opcao == "8":
            codigo = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade a ser atualizada (use negativo para diminuir): "))
            atualizar_estoque(estoque, codigo, quantidade)
        elif opcao == "9":
            codigo = int(input("Digite o código do produto: "))
            novo_preco = float(input("Digite o novo preço de venda: "))
            atualizar_preco_venda(estoque, codigo, novo_preco)
        elif opcao == "10":
            calcular_valor_total_estoque(estoque)
        elif opcao == "11":
            calcular_lucro_presumido(estoque)
        elif opcao == "12":
            gerar_relatorio_geral(estoque)
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")


# Simulação de um estoque inicial com os dados fornecidos no enunciado
estoque_inicial = "mouse;100;23;12.75;22.50#teclado;101;14;47.80;95.70#monitor;102;7;398.75;790.50#impressora;103;0;347.75;780.50"
estoque = carregar_estoque_inicial(estoque_inicial)

# Iniciar o menu interativo
menu(estoque)
