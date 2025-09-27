import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Extract
print('\n', '=' * 20, ' Extract ', '=' * 20)

dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print(f'\n>> Nome colunas dados_empresaA: {dados_empresaA.nome_colunas}')
print(f'>> Qtd linhas dados_empresaA: {dados_empresaA.qtd_linhas}')
print(f'\n>> Nome colunas dados_empresaB: {dados_empresaB.nome_colunas}')
print(f'>> Qtd linhas dados_empresaB: {dados_empresaB.qtd_linhas}')

# Transform
print('\n', '=' * 20, ' Transform ', '=' * 20)

key_mapping = {
    # De : Para
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(f'\n>> Nome colunas dados_empresaB RENOMEADO: {dados_empresaB.nome_colunas}')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'\n>> Nome colunas dados_fusao: {dados_fusao.nome_colunas}')
print(f'>> Qtd linhas dados_fusao: {dados_fusao.qtd_linhas}')

# Load
print('\n', '=' * 20, ' Load ', '=' * 20)

dados_fusao.salvando_dados(path_dados_combinados)
print(f'\n>> Salvando dados_fusao em: {path_dados_combinados}\n')