import matplotlib.pyplot as plt
import math

def sin_function(subplot,title):
    x_sin = []
    y_sin = []

    for cont in range (70):
        x_sin.append(cont/10)
        y_sin.append(math.sin(cont/10))

    plt.sca(subplot)

    plt.xlim(-0.01,6.29)
    plt.ylim(-2.01,2.01)

    plt.yticks([-1.5,-1,-0.5,0,0.5,1,1.5])
    plt.xticks([0,1.57,3.14,4.71,6.28])
    plt.title(title)

    plt.plot([0,10],[0,0],color="black")
    plt.plot(x_sin,y_sin,color="red",label="Senoíde")