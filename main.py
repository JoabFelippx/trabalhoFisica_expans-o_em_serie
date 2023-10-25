import math
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

sum = 0
doty = []
dotx = [0]
x = 0

def funSen(x):
    return math.sin(x)

def funCos(x):
    return math.cos(x)

def maclurin(func: str, lim: float, n: int):

    global sum
    global x
    a = 0

    if func == 'sin':

        while (x <= lim):
            
            for i in range(0,n):
                sum += ((-1) ** (i)) * (x ** (2 * i + 1)) / math.factorial(2*i+1)

            doty.append(sum)             
            print(f'a: {a} - Ponto: {x} - Suma: {sum}')
            a = a + 1
            sum = 0
            x += math.pi / 10
            dotx.append(x)

    elif func == 'cos':

        while (x <= lim):
            for i in range(0,n):
                sum += ((-1) ** (i)) * (x ** (2 * i)) / math.factorial(2*i)
            doty.append(sum)          
            print(f'a: {a} - Ponto: {x} - Suma: {sum}')
            a = a + 1
            sum = 0
            x += math.pi / 10
            dotx.append(x)



maclurin('cos', 2 * math.pi, 10)
del dotx[-1]
print(dotx)
print(doty)
