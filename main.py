import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sympy import *


doty = []
dotx = []
f = 'quadripole' #['cos', 'sin', 'exp', quadripole]

x_exp = Symbol('x')
u = Symbol('u')
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
  'quadripole': {
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
  }

}

def maclurin(func: str):

    for n in [5, 10, 30]:

        x = 0
        sum = 0

        if func == 'sin':
            lim = 2*math.pi
            while (x <= lim):

                for i in range(0,n):
                    sum += ((-1) ** (i)) * (x ** (2 * i + 1)) / math.factorial(2*i+1)

                #print(f'a: {a} - Ponto: {x} - Suma: {sum}')

                dictfuncs[func][n]['y'].append(sum)  
                dictfuncs[func][n]['x'].append(x)

                x += math.pi / 10
                sum = 0            

        elif func == 'cos':
            lim = 4
            while (x <= lim):

                for i in range(0,n):
                    sum += ((-1) ** (i)) * (x ** (2 * i)) / math.factorial(2*i)

                #print(f'a: {a} - Ponto: {x} - Soma: {sum}')

                dictfuncs[func][n]['y'].append(sum) 
                dictfuncs[func][n]['x'].append(x)

                x += math.pi / 10
                sum = 0
               

        elif func == 'exp':
            
            while (x <= lim):
              
              for i in range(0, n):
                
                sum += (diff(func_exp, x_exp, i).subs(x_exp, 0) * (x_exp ** i)) / math.factorial(i)
                sum = sum.subs(x_exp, x)
              dictfuncs[func][n]['y'].append(sum) 
              dictfuncs[func][n]['x'].append(x)

              x += 4 / 20
              sum = 0
              
        
        elif func == 'quadripole':
            x = 0.00000000000000000000000000001
            lim = 1
            while (x < lim):
                y = 1/x
                for i in range(0, n):
                    
                    g = (1+u) ** ((i+1))
                    f = (1-u) ** ((i+1))

                    g_diff = diff(g, u) / factorial(i)
                    f_diff = diff(f, u) / factorial(i)
                    diff_sum = f_diff.subs(u, 0) * (u ** i) + g_diff.subs(u, 0) * (u ** i)
                    diff_sum.subs(u, x)
                    sum += diff_sum - (2* (x **(2)))
                    
                    if n == 30:
                        # print(f'{sum}')
                        pass
                    # eq = eq.subs(u, x)
                
                dictfuncs[func][n]['y'].append(sum)
                dictfuncs[func][n]['x'].append(x)
                
                x += 1/20 
                sum = 0          
            
maclurin(f)

fig, ax = plt.subplots()



def update(i):

    ax.clear()
    a = np.subtract(np.add(np.power(np.add(1, dictfuncs[f][30]['x'][:i]), -2), np.power(np.subtract(1, dictfuncs[f][30]['x'][:i]), -2)),np.multiply(2, np.power(dictfuncs[f][30]['x'][:i], 2)))
    print(a)
    print(dictfuncs[f][30]['y'][:i])
    if f == 'exp':
        ax.set_xlim([0,3.85])
        ax.set_ylim([0,0.55])
    elif f == 'quadripole':
        ax.set_xlim([0,1])
        ax.set_ylim([-200,100])
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
    elif f == 'quadripole':
         ax.plot(dictfuncs[f][30]['x'][:i],  a, color='orange', linestyle= '-', marker= 'x')

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(dictfuncs[f][5]['x']), interval=45, repeat=False)
plt.show()
