euler = 2.718281828


def triangular (x,pert):
    a = pert[0]
    m = pert[1]
    b = pert[2]

    if x<=a:
        return 0
    elif x>b:
        return 0
    elif x<m:
        return (x-a)/(m-a)
    else:
        return (b-x)/(b-m)
    
def trapezoidal(x,pert):
    a = pert[0]
    m = pert[1]
    n = pert[2]
    b = pert[3]

    if x<=a:
        return 0
    elif x>b:
        return 0
    elif x<=m:
        return (x-a)/(m-a)
    elif x<=n:
        return 1
    else:
        return (b-x)/(b-n)
    
def gaussiana(x,pert):
    m = pert[0]
    k = pert[1]
    
    if k<0:
        return 0
    else:
        return pow(euler,-k*pow(x-m,2))