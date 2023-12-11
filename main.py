import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sympy import *


doty = []
dotx = []
f = 'dipole' #['cos', 'sin', 'exp', quadripole, dipole]

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
  },
  'dipole': {
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

def mkDotdata(func, n,dots_x, dots_y):
    with open(f'{func}_{n}_data.dat', 'w') as f:
        for dot in range(len(dots_x)):
            f.write(f'{dots_x[dot]} {dots_y[dot]}\n')    


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

            mkDotdata(func, n, dictfuncs[func][n]['x'], dictfuncs[func][n]['y'])

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

            mkDotdata(func, n, dictfuncs[func][n]['x'], dictfuncs[func][n]['y'])
               

        elif func == 'exp':
            lim = 4
            while (x <= lim):
              
              for i in range(0, n):
                
                sum += (diff(func_exp, x_exp, i).subs(x_exp, 0) * (x_exp ** i)) / math.factorial(i)
                sum = sum.subs(x_exp, x)
              dictfuncs[func][n]['y'].append(sum) 
              dictfuncs[func][n]['x'].append(x)

              x += 4 / 20
              sum = 0
            mkDotdata(func, n, dictfuncs[func][n]['x'], dictfuncs[func][n]['y'])
        elif func == 'dipole':
            diff_sum = 0          
            x = 1
            lim = 0
            while lim < 20:
                y = 1/2*x
                for i in range(0, n):
                    
                    g = (u) ** ((i+1))
                    f = (u) ** ((i+1))

                    g_diff = diff(g, u) 
                    f_diff = diff(f, u) * ((-1) ** (i))
                    
                    diff_sum += f_diff - g_diff
                    diff_sum = diff_sum.subs(u, x)

                dictfuncs[func][n]['y'].append(diff_sum)
                dictfuncs[func][n]['x'].append(y)
                x += 1/20 
                print(y)
                diff_sum = 0          
                lim += 1

            dictfuncs[func][n]['y'] = dictfuncs[func][n]['y']
            mkDotdata(func, n, dictfuncs[func][n]['x'], dictfuncs[func][n]['y'])

        elif func == 'quadripole':
            diff_sum = -2
            x = 0.00000000000000000000000000001
            lim = 1
            while (x < lim):
                y = 1/1*x
                for i in range(0, n):
                    
                    g = (u) ** ((i+1))
                    f = (u) ** ((i+1))

                    g_diff = diff(g, u) 
                    f_diff = diff(f, u) * ((-1) ** (i))
                    
                    diff_sum += f_diff + g_diff
                    diff_sum = diff_sum.subs(u, x)
                
                dictfuncs[func][n]['y'].append(diff_sum)
                dictfuncs[func][n]['x'].append(y)
                x += 1/20 
                print(y)
                diff_sum = -2          

            dictfuncs[func][n]['y'] = dictfuncs[func][n]['y'][::-1]
            mkDotdata(func, n, dictfuncs[func][n]['x'], dictfuncs[func][n]['y'])


maclurin(f)

fig, ax = plt.subplots()


def update(i):

    ax.clear()

    if f == 'quadripole':
        a = np.subtract(np.add(np.power(np.add(1, dictfuncs[f][30]['x'][:i]), -2), np.power(np.subtract(1, dictfuncs[f][30]['x'][:i]), -2)),2)[::-1]
        #print(a)
        print(dictfuncs[f][30]['y'][:i])
        pass

    if f == 'exp':
        ax.set_xlim([0,3.85])
        ax.set_ylim([-0.55,0.55])
    elif f == 'quadripole':
        # ax.set_xlim([0,1])
        # ax.set_ylim([-200,100])
        pass
    elif f == 'dipole':
        # ax.set_xlim([0,0.5])
        # ax.set_ylim([-20,0])
        b = np.subtract(np.power(np.add(1, dictfuncs[f][30]['x'][:i]), -2), np.power(np.subtract(1, dictfuncs[f][30]['x'][:i]), -2))
        print(b)
    else:  
        ax.set_xlim([0,7])
        ax.set_ylim([-5,10])

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
    elif f == 'dipole':
        ax.plot(dictfuncs[f][30]['x'][:i],  b, dictfuncs[f][30]['x'][:i], color='orange', linestyle= '-', marker= 'x')         
        pass


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(dictfuncs[f][5]['x']), interval=45, repeat=False)
plt.show()
