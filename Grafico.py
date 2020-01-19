import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("a11_CONSUMO.csv")
plt.subplot(1,2,1)
dataset.boxplot()
plt.title('Boxplot')

plt.subplot(1,2,2)
labels = dataset.data
plt.plot(dataset.data, dataset.consumo,'red')
    
plt.xticks(dataset.data,labels, rotation = 'vertical')
plt.xlabel('datas',color = 'blue')
plt.ylabel('consumo')
plt.grid(True)
plt.margins(0.2)
plt.title('O consumo')

plt.show()
   
