import csv

datas = []
lucros = []

with open('C:/Users/Deangellis/Desktop/Next dados/Mini Projeto Financeiro/dados_financeiros.csv', 'r', encoding='utf-8') as arquivo:
    
    leitor = csv.reader(arquivo)

    # Ignora o cabeçalho
    next(leitor)

    # Percorrer as linhas do arquivo
    for linha in leitor:
        data = linha[0]
        lucro = int(linha[1])

        datas.append(data)
        lucros.append(lucro)

# Total de meses
total_meses = len(datas)

# Total liquido
total_liquido = sum(lucros)

# Média dos lucros / perdas
media_lucros = total_liquido / total_meses

# Lista para armazenar mudanças
mudancas = []

# Calculando as mudanças entre meses
for i in range(1, len(lucros)):
    diferenca = lucros[i] - lucros[i - 1]
    mudancas.append(diferenca)

# Média das mudanças
media_mudancas = sum(mudancas) / len(mudancas)

# Maior aumento nos lucros
maior_aumento = max(mudancas)
indice_aumento = mudancas.index(maior_aumento)
data_aumento = datas[indice_aumento + 1]

# Maior redução nos lucros
maior_reducao = min(mudancas)
indice_reducao = mudancas.index(maior_reducao)
data_reducao = datas[indice_reducao + 1]

# Exibindo os resultados
print("Análise Financeira")
print("-" * 30)

print(f"Total de Meses: {total_meses}")
print(f"Total Líquido: R${total_liquido}")

print(f"Média dos Lucros/Perdas: R${media_lucros:.2f}")
print(f"Média das Mudanças: R${media_mudancas:.2f}")

print(f"Maior Aumento nos Lucros: {data_aumento} (R${maior_aumento})")
print(f"Maior Redução nos Lucros: {data_reducao} (R${maior_reducao})")