import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sympy import *


doty = []
dotx = []
f = 'cos' #['cos', 'sin', 'exp']

x_exp = Symbol('x')
func_exp = x_exp * exp(-2*x_exp)

dictfuncs = {
    'cos': {
        5:{
            'x':[],
            'y':[]
        },
        10:{
            'x':[],
            'y':[]
        },
        30:{
            'x':[],
            'y':[]
        }
    },
    'sin': {
        5:{
            'x':[],
            'y':[]
        },
        10:{
            'x':[],
            'y':[]
        },
        30:{
            'x':[],
            'y':[]
        }
    },
  'exp': {
      5:{
          'x':[],
          'y':[]
      },
      10:{
          'x':[],
          'y':[]
      },
      30:{
          'x':[],
          'y':[]
      }
  },

}

def maclurin(func: str):
    if func == 'exp':
        lim = 4

    else:
        lim = 2*math.pi

    for n in [5, 10, 30]:

        x = 0
        sum = 0
        a = 0
        if func == 'sin':

            while (x <= lim):

                for i in range(0,n):
                    sum += ((-1) ** (i)) * (x ** (2 * i + 1)) / math.factorial(2*i+1)

                #print(f'a: {a} - Ponto: {x} - Suma: {sum}')

                dictfuncs[func][n]['y'].append(sum)  
                dictfuncs[func][n]['x'].append(x)

                x += math.pi / 10
                sum = 0
                a = a + 1

        elif func == 'cos':

            while (x <= lim):

                for i in range(0,n):
                    sum += ((-1) ** (i)) * (x ** (2 * i)) / math.factorial(2*i)

                #print(f'a: {a} - Ponto: {x} - Soma: {sum}')

                dictfuncs[func][n]['y'].append(sum) 
                dictfuncs[func][n]['x'].append(x)

                x += math.pi / 10
                sum = 0
                a = a + 1

        elif func == 'exp':

            while (x <= lim):
              
              for i in range(0, n):
                
                sum += (diff(func_exp, x_exp, i).subs(x_exp, 0) * (x_exp ** i)) / math.factorial(i)
                sum = sum.subs(x_exp, x)
              dictfuncs[func][n]['y'].append(sum) 
              dictfuncs[func][n]['x'].append(x)

              x += 4 / 20
              sum = 0
              a = a + 1


maclurin(f)

fig, ax = plt.subplots()

def update(i):

    ax.clear()
    if f == 'exp':
      ax.set_xlim([0,3.85])
      ax.set_ylim([0,0.55])
    else:  
      ax.set_xlim([0,7])
      ax.set_ylim([-1,15])
    ax.plot(dictfuncs[f][5]['x'][:i], dictfuncs[f][5]['y'][:i], color='red', linestyle= '', marker='*')
    ax.plot(dictfuncs[f][10]['x'][:i], dictfuncs[f][10]['y'][:i], color='blue', linestyle= '', marker='h')
    ax.plot(dictfuncs[f][30]['x'][:i], dictfuncs[f][30]['y'][:i], color='green', linestyle= '', marker='o')

    if f == 'exp':
        ax.plot(dictfuncs[f][30]['x'][:i], np.multiply(dictfuncs[f][30]['x'][:i], np.float_power(math.e, (np.multiply(-2, dictfuncs[f][30]['x'][:i])))), color='orange', linestyle= '', marker= 'x')
    elif f == 'sin':
        ax.plot(dictfuncs[f][30]['x'][:i], np.sin(dictfuncs[f][30]['x'][:i]), color='orange', linestyle= '', marker= 'x')
    elif f == 'cos':
        ax.plot(dictfuncs[f][30]['x'][:i],  np.cos(dictfuncs[f][30]['x'][:i]), color='orange', linestyle= '', marker= 'x')

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(dictfuncs[f][5]['x']), interval=45, repeat=False)
plt.show()
