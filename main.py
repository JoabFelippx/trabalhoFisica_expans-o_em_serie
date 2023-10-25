import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


doty = []
dotx = []
f = 'cos' #['cos', 'sin', 'exp']

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
    }

}

def maclurin(func: str, lim: float, n: int):

    for n in [5, 10, 30]:
        
        x = 0.0
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



maclurin(f, 2 * math.pi, 10)

fig, ax = plt.subplots()

def update(i):

    ax.clear()
    ax.set_xlim([0,10])
    ax.set_ylim([-1,11.5])
    ax.plot(dictfuncs[f][5]['x'][:i], dictfuncs[f][5]['y'][:i], color='red')
    ax.plot(dictfuncs[f][10]['x'][:i], dictfuncs[f][10]['y'][:i], color='blue')
    ax.plot(dictfuncs[f][30]['x'][:i], dictfuncs[f][30]['y'][:i], color='green')

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(dictfuncs[f][5]['x']), interval=45, repeat=False)
plt.show()
