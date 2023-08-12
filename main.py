def carregar_dados(file_path):
    try:
        with open(file_path, 'r') as arquivo:
            linhas = arquivo.readlines()
            colunas = linhas[0].strip().split(',')
            dados = [linha.strip().split(',') for linha in linhas[1:]]

            for entrada in dados:
                for i, coluna in enumerate(colunas):
                    if "Rate" in coluna:
                        indice_rate = i
                        if indice_rate < len(entrada):
                            entrada[indice_rate] = entrada[indice_rate].strip('"')

            return colunas, dados
    except FileNotFoundError:
        return None, None



def calcular_media_avaliacao(dados, indice_empresa, indice_avaliacao):
    total_marvel = 0
    total_dc = 0
    contagem_marvel = 0
    contagem_dc = 0

    for entrada in dados:
        if entrada[indice_empresa] == "Marvel":
            total_marvel += float(entrada[indice_avaliacao])
            contagem_marvel += 1
        elif entrada[indice_empresa] == "DC":
            total_dc += float(entrada[indice_avaliacao])
            contagem_dc += 1

    media_marvel = total_marvel / contagem_marvel if contagem_marvel > 0 else 0
    media_dc = total_dc / contagem_dc if contagem_dc > 0 else 0

    return media_marvel, media_dc

def calcular_total(dados, indice_empresa, indice_valor):
    total_marvel = 0
    total_dc = 0

    for entrada in dados:
        if entrada[indice_empresa] == "Marvel":
            total_marvel += float(entrada[indice_valor])
        elif entrada[indice_empresa] == "DC":
            total_dc += float(entrada[indice_valor])

    return total_marvel, total_dc






# opçao numero 1 
def analisar_avaliacao(dados, colunas):
    indice_empresa = colunas.index("Company")
    indice_avaliacao = colunas.index("Rate")
    media_marvel, media_dc = calcular_media_avaliacao(dados, indice_empresa, indice_avaliacao)

    print("\nMédia de Avaliações:")
    print("Marvel:", media_marvel)
    print("DC:", media_dc)
    
    vencedor = "Marvel" if media_marvel > media_dc else "DC"
    print(f"Quem vence nesse quesito: {vencedor}")




#opçao numero 2
def comparar_total_orcamento(dados, colunas):
    indice_empresa = colunas.index("Company")
    indice_orcamento = colunas.index("Budget")
    total_marvel, total_dc = calcular_total(dados, indice_empresa, indice_orcamento)

    print("\nTotal de Orçamentos:")
    print("Marvel:", total_marvel)
    print("DC:", total_dc)
    
    vencedor = "Marvel" if total_marvel > total_dc else "DC"
    print(f"Quem vence nesse quesito: {vencedor}")





#opçao numero 3
def comparar_total_faturamento(dados, colunas):
    indice_empresa = colunas.index("Company")
    indice_faturamento = colunas.index("Gross Worldwide")
    total_marvel, total_dc = calcular_total(dados, indice_empresa, indice_faturamento)

    print("\nTotal de Faturamentos:")
    print("Marvel:", total_marvel)
    print("DC:", total_dc)
    
    vencedor = "Marvel" if total_marvel > total_dc else "DC"
    print(f"Quem vence nesse quesito: {vencedor}")



    #opçao numero 4

def filtrar_por_avaliacao(dados, colunas):
    limiar_avaliacao = float(input("Informe a nota mínima desejada: "))
    indice_avaliacao = colunas.index("Rate")
    
    filmes_filtrados = [entrada for entrada in dados if float(entrada[indice_avaliacao]) >= limiar_avaliacao]
    print("\nFilmes com Avaliação maior ou igual a", limiar_avaliacao)
    for entrada in filmes_filtrados:
        print(entrada)

def main():
    caminho_arquivo = input("Informe o caminho do arquivo CSV: ")
    colunas, dados = carregar_dados(caminho_arquivo)

    if colunas is None or dados is None:
        print("Caminho do arquivo não encontrado.")
        return 
    

    colunas = [coluna.strip('"') for coluna in colunas]  # Remover aspas duplas dos cabeçalhos

    while True:
        print("--------ESCOLHA SUA OPÇÃO-------------------")
        print("1. Avaliação do público")
        print("2. Orçamento")
        print("3. Faturamento")
        print("4. Filtrar filmes por avaliação")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            analisar_avaliacao(dados, colunas)
        elif opcao == '2':
            comparar_total_orcamento(dados, colunas)
        elif opcao == '3':
            comparar_total_faturamento(dados, colunas)
        elif opcao == '4':
            filtrar_por_avaliacao(dados, colunas)
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")
if __name__ == "__main__":
    main()
