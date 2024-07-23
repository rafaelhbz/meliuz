import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_de_dados = pd.read_excel("Todos_tweets.xlsx")


remove_espaco = base_de_dados["Tweets"].str.replace(' ','')
contar_palavras = remove_espaco.value_counts()


top_10_palavras = contar_palavras[:10]

plt.figure(figsize=(10,5))
bar_plot = sns.barplot(top_10_palavras, top_10_palavras.index, alpha=0.8).set_title("Top 10 words")
#bar_plot.set(xlabel='tweets', ylabel='quantidade')
fig = bar_plot.get_figure()
fig.savefig("out.png")
#plt.title('Top 10 words mentioned')
#plt.ylabel('Palavras do Tweet', fontsize=12)
#plt.xlabel('Número de palavras', fontsize=12)
#plt.show()

#plt.savefig('meuGrafico.png') #esta linha cria um arquivo png com o gráfico
