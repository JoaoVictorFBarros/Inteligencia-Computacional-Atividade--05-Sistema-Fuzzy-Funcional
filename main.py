import matplotlib.pyplot as plt
from sin_function import sin_function
from entry_fuzzyfication import entry_fuzzyfication_graph, fuzzyfy_value
from rules import output_activation_0_order, find_params_0_order


fig, axs = plt.subplots(2, 1,figsize=[9,9])
plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05, hspace=0.3)

entry_fuzzyfication_graph(axs[0])

sin_function(axs[1],"Takagi-Sugeno de ordem 0")
plt.sca(axs[1])

x = [i * 0.1 for i in range(0, int(7 / 0.1) + 1)]

y = []

params = find_params_0_order()

for value in x:
    y.append(output_activation_0_order(fuzzyfy_value(value),value,params))

plt.plot(x,y,label="Aproximação")
plt.legend(loc="upper right")

plt.show()