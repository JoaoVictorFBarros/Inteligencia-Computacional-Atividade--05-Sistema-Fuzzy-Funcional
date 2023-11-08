import matplotlib.pyplot as plt
from utilities.funcoes_pertinencia import gaussiana

entry_k = 1/5

low = [0,entry_k]
mid = [3.14,entry_k]
high = [6.28,entry_k]

x = [i * 0.1 for i in range(0, int(7 / 0.1) + 1)]

labels = ["Baixo","Médio","Alto"]

functions = [low,mid,high]

def fuzzyfy_value(value):
    values = []

    for function in functions:
        values.append(gaussiana(value,function))
    
    return values

def entry_fuzzyfication_graph(subplot):
    colors = ["red","orange","green","blue","purple"]

    for index,function in enumerate(functions):

        y = []
        for point in x:
            y.append(gaussiana(point,function))
            
        plt.sca(subplot)  

        plt.xlim(-0.01,6.29)
        plt.ylim(-0.01,1.01)
        plt.xticks([0,1.57,3.14,4.71,6.28])
        plt.title("Funções de pertinência da entrada")

        plt.plot(x,y,color=colors[index],label=labels[index])

        plt.legend(loc="lower right")