# Primeiro exemplo de manipulação de dados usando python pandas
#python -m pip install pandas - (comando para o console)

#Importanto biblioteca pandas no python
import pandas as pd


combustiveis_df = pd.read_excel("ca-2021-02.xlsx")



#Usa o display  para ver o dataframe
display(combustiveis_df)

#Exibe as primeiras 5 linhas
display(combustiveis_df.head())

#Quero na verdade exibir as 15 primeiras 15 linhas
display(combustiveis_df.head(15))

#Comnados dataframe.shape e dataframe.describe()

print(combustiveis_df.shape)
#mostra o numero de linhas e colunas

#Só as linhas
print(combustiveis_df.shape[0])

#Quais são as colunas e que tipo de dados cada um tem...
print(combustiveis_df.info())

#Describe() mostra as estatisticas mais basicas que a gente precisa
print(combustiveis_df.describe())