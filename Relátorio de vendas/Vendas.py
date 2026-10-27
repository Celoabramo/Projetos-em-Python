import csv

caminho = "vendas.csv"

vendas=[]
erros=[]
linhas = []
por_produto={}

def carregar_vendas(): #Lendo as Vendas
    with open(caminho,"r", encoding="utf-8", newline=""  ) as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            linha["Quantidade"] = int(linha["Quantidade"])
            linha["Preco"] = float(linha["Preco"])
            vendas.append(linha)

def erros_lista(): #Armazenando erros e Validando os dados
    if not vendas:
        erros.append("Erro: Nenhuma venda foi carregada")
    else:
        for indice, venda in enumerate(vendas):
            produto = venda.get("Produto", "").strip()
            if not produto:
                erros.append(f'Linha {indice+1}:Produto inválido!')
            if venda["Quantidade"] <= 0:
                erros.append(f'Linha {indice+1}:Quantidade deve ser >0')
            if venda["Preco"] <= 0:
                erros.append(f'Linha {indice+1}: Quantidade deve ser >0')
    if erros:
         for erro in erros:
            print(erro)
            print("=====================================================================")
    else:
        print("Vendas carregadas com sucesso!\n","==============================================")


def calculo_valores():#Calculando os Valores
    for venda in vendas:
        venda["ValorTotal"] = venda["Quantidade"] * venda["Preco"]

    totalregistros = len(vendas)
    totalunidades = sum(venda["Quantidade"] for venda in vendas)
    valortotal = sum(venda["ValorTotal"] for venda in vendas)
    valor_medio_por_venda = valortotal / totalunidades

    return totalregistros, totalunidades, valor_medio_por_venda , valortotal


def agrupar_produto():
    for venda in vendas:
        venda["ValorTotal"] = venda["Quantidade"] * venda["Preco"]
        produto = venda["Produto"]
        if produto not in por_produto:
            por_produto[produto] = {"Quantidade_total": 0 , "ValorTotal": 0.0}
        por_produto[produto]["Quantidade_total"] += venda["Quantidade"]
        por_produto[produto]["ValorTotal"] +=  venda["ValorTotal"]
    print(f'total de produtos: {len(por_produto)}')
    print(por_produto)


def destaque():
    produto_maiorqtd = None

    maiorqtd = 0
    for produto, dados in por_produto.items():
        if dados["Quantidade_total"] > maiorqtd:
            maiorqtd = dados["Quantidade_total"]
            produto_maiorqtd = (produto, dados)

    produto_maiorvlr =None
    maiorvlr = 0
    for produto, dados in por_produto.items():
        if dados["ValorTotal"] > maiorvlr:
            maiorvlr = dados["ValorTotal"]
            produto_maiorvlr = (produto, dados)
    p_qtd , d_qtd = produto_maiorqtd
    p_vlr , d_vlr = produto_maiorvlr
    return p_qtd , d_qtd,  p_vlr , d_vlr 

def relatorio():
    destaques = destaque()
    p_qtd, d_qtd, p_vlr, d_vlr = destaques
    totais = calculo_valores()
    totalregistros, totalunidades, valor_medio_por_venda, valortotal = totais
    linhas.append("=" * 60)
    linhas.append("RELATÓRIO DE VENDAS")
    linhas.append("=" * 60)
    linhas.append("ESTATÍSTICAS GERAIS")
    linhas.append("=" * 60)
    linhas.append(f"Total de registros: {totalregistros}")
    linhas.append(f"Total de unidades vendidas: {totalunidades}")
    linhas.append(f"Valor total: R$ {valortotal:,.2f}")
    linhas.append(f"Valor médio por venda: R$ {valor_medio_por_venda:,.2f}")
    linhas.append("=" * 60)
    linhas.append("DESTAQUES")
    linhas.append("=" * 60)
    linhas.append(f"Produto com maior quantidade: {p_qtd} ({d_qtd['Quantidade_total']} unidades)")
    linhas.append(f"Produto com maior faturamento: {p_vlr} (R$ {d_vlr['ValorTotal']:.2f})")
    linhas.append("=" * 60)
    linhas.append("DETALHAMENTO POR PRODUTO (por faturamento)")
    linhas.append("=" * 60)
    produtos_ordenados = sorted( [(dados["ValorTotal"], produto, dados) for produto, dados in por_produto.items()], reverse=True)
    for valortotal, produto, dados in produtos_ordenados:
        linhas.append(f"{produto}: {dados['Quantidade_total']} unidades - R$ {dados['ValorTotal']:.2f}")
    linhas.append("=" * 60)
    linhas.append("Fim do relatório")
    linhas.append("=" * 60)




#Ordem de processamento dos dados
carregar_vendas()
erros_lista()
calculo_valores()
agrupar_produto()

print("=========================================================")
print("total de vendas carregadas", len(vendas))
print("Vendas:")
for venda in vendas:
    print(f'\n {venda}')
print('\nPROCESSAMENTO DE DADOS FEITO ', '\n ', '\n')
#Criação do relátorio
relatorio()

texto_relatorio = "\n".join(linhas)

print(texto_relatorio)

with open("Relátorio_de_vendas.txt", "w",encoding = "utf-8") as file:
    file.write(texto_relatorio)
print("RELATÓRIO SALVO COM SUCESSO (Relátorio_de_vendas.txt)")
