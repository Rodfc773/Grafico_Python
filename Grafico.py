import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Consumo.csv")

#Gera um boxplot dos dados
dataset.boxplot()
plt.title('Boxplot')
plt.show()

#Gera um gráfico com os 10 primeiros dados do arquivo
plt.style.use('dark_background')
labels = dataset.data
plt.subplot(1,2,1)
plt.plot(dataset.data[:10], dataset.consumo[:10],'green')
plt.xticks(dataset.data[:10],labels, rotation = 'vertical')
plt.xlabel('datas')
plt.ylabel('consumo')
plt.grid(True)
plt.margins(0.2)
plt.title('Consumo de 1984')


#Gera o gráfico dos ultimos 10 dados
plt.subplot(1,2,2)
plt.plot(dataset.data[145:], dataset.consumo[145:], 'green')
plt.xticks(dataset.data[145:154], dataset.data, rotation = 'vertical')
plt.xlabel('datas')
plt.ylabel('Consumo')
plt.grid(True)
plt.title('Consumo de 1996')
plt.show()

#Gera o gráfico dos 30 primeiros dados
plt.plot(dataset.data[:30], dataset.consumo[:30], 'green')
plt.xticks(dataset.data[:30], dataset.data, rotation = 'vertical')
plt.xlabel('datas')
plt.ylabel('Quantidade consumida')
plt.grid(True)
plt.title('Consumo entre os anos de 1984 e 1986')
plt.show()
   
