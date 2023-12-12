import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


#Lista de pontos para plotar o gráfico
dotx_5 = []
doty_5 = []

dotx_10 = []
doty_10 = []

dotx_30 = []
doty_30 = []

#Simbolos para o sympy
x_exp = Symbol('x')
u = Symbol('u')

#Função exponecial
func_exp = x_exp * exp(-2*x_exp)

#Função para escrever os pontos no arquivo .dat
def mkDotFile(func, n, dotsx, dotsy):
    with open(f'{func}_{n}.dat', 'w') as file:
        for dot in range(len(dotsx)):
            file.write(f'{dotsx[dot]} {dotsy[dot]}\n')

def createList(n, x, sum):

    global dotx_5, doty_5, dotx_10, doty_10, dotx_30, doty_30

    if n == 5:
        dotx_5.append(x)
        doty_5.append(sum)

    elif n == 10:
        dotx_10.append(x)
        doty_10.append(sum)
    else:
        dotx_30.append(x)
        doty_30.append(sum)

def real_Func(func,x):

    if func == 'sin':
        return np.sin(x)
    elif func == 'cos':
        return np.cos(x)
    elif func == 'exp':
        return np.multiply(x, np.float_power(math.e, (np.multiply(-2, x))))    
    elif func == 'dipole':
        return  np.subtract(np.power(np.add(1, x), -2),np.power(np.subtract(1, x), -2))
    elif func == 'quadripole':
        return  np.subtract(np.add(np.power(np.add(1, x), -2), np.power(np.subtract(1, x), -2)),2)
    
def expan_sin():

    for n in [5, 10, 30]:

        x = 0
        sum = 0
        limit = 2*math.pi

        while x <= limit:

            for k in range(0, n):
                sum += ((-1)**k)*(x**(2*k + 1))/math.factorial(2*k + 1)
        
            createList(n, x, sum)
            x += math.pi/10
            sum = 0


def expan_cos():

    for n in [5, 10, 30]:

        x = 0
        sum = 0
        limit = 2*math.pi

        while x <= limit:

            for k in range(0, n):
                sum += ((-1)**k)*(x**(2*k))/math.factorial(2*k)


            createList(n, x, sum)
            x += math.pi/10
            sum = 0


def expan_exp():
    
    for n in [5, 10, 30]:
        
        x = 0
        sum = 0
        limit = 4

        while x <= limit:
            

            for k in range(0, n):
                sum += (diff(func_exp, x_exp, k).subs(x_exp, 0)*(x_exp**k))/math.factorial(k)
                sum = sum.subs(x_exp, x)

            createList(n, x, sum)
            x += 0.1
            sum = 0


def expan_dipole():

    for n in [5, 10, 30]:
        x = 0.000000000000001
        sum = 0
        limit = 1
        while x <= limit:

            for k in range(n):

                func_f = u ** (k+1)
                func_g = func_f # u ** (n + 1)

                f_diff = diff(func_f, u) * ((-1)**(k))
                g_diff = diff(func_g, u)

                sum += f_diff - g_diff
                sum = sum.subs(u, x)

            createList(n, x, sum)
            x += 1/20
            sum = 0

def expan_quadripole():

    for n in [5, 10, 30]:
        x = 0.000000000000001
        sum = 0
        limit = 1
        while x <= limit:

            for k in range(n):

                func_f = u ** (k + 1)
                func_g = func_f # u ** (n + 1)

                f_diff = diff(func_f, u)
                g_diff = diff(func_g, u) * ((-1)**(k))

                sum += f_diff + g_diff
                sum = sum.subs(u, x)

            createList(n, x, sum)
            x += 1/20
            sum = 0


f = input('Digite a função: ')

if f == 'sin':
    expan_sin()
elif f == 'cos':
    expan_cos()
elif f == 'exp':
    expan_exp()
elif f == 'dipole':
    expan_dipole()
elif f == 'quadripole':
    expan_quadripole()
else:
    print('Função não encontrada')


if f == 'dipole' or f == 'quadripole':

    doty_5 = doty_5[::-1]
    doty_10 = doty_10[::-1]
    doty_30 = doty_30[::-1]

mkDotFile(f, 5, dotx_5, doty_5)
mkDotFile(f, 10, dotx_10, doty_10)
mkDotFile(f, 30, dotx_30, doty_30)

plt.plot(dotx_5, doty_5, color='red', linestyle= '', marker='*', label='n = 5')
plt.plot(dotx_10, doty_10, color='green', linestyle= '', marker='h', label='n = 10')
plt.plot(dotx_30, doty_30, color='blue', linestyle= '', marker='o', label='n = 30')
plt.plot(dotx_30, real_Func(f, dotx_30)[::-1], color='yellow', linestyle= '-', label=f)

plt.legend()
plt.show()

