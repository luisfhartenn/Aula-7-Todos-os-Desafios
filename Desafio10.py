def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        # Validação para garantir que 'dados' existe e tem as chaves necessárias
        if not dados or "nome" not in dados or "quantidade" not in dados:
            return "Erro: Dados incompletos. 'nome' e 'quantidade' são obrigatórios."
        return post_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/buscar" and metodo == "GET":
        # Validação para garantir que 'dados' existe e tem a chave 'nome'
        if not dados or "nome" not in dados:
            return "Erro: O parâmetro 'nome' é obrigatório para a busca."
        return get_produto_por_nome(dados["nome"])

    # Retorno padrão de fallback (Tratamento de rota não encontrada)
    return "Erro: Rota ou método não encontrados."