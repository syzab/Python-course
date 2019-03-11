from sys import argv
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

# 1
print(10*'-','##1')

xl = list(range(56,101,1))

for x in xl:
    y = 2*(x**2) + 2*x + 2
    print('y =',y,'| x =',x)

# 2 
print(10*'-','##2')

t=0
while(t==0):
    t=1
    x=input('Input number: ')
    try:
        val = int(x)
    except ValueError:
        print("Number must be int")
        t=0
       
        
x=int(x)

fact=1


for i in range(1,abs(x)+1):
    fact=fact*i
        
if x<0: 
    fact = -fact
    
    
print("Factorial of ",x," = ",fact)

# 3
print(10*'-','##3')


#print(inpa)

def min_array(x):
    inpa = inp.split(',')
    for i in range(0,len(inpa)):
        inpa[i] = inpa[i].replace(" ", "")
        print(inpa[i], 'idx: ',i)

    lmin = inpa[0]
    lind=[]
    for i in range (0,len(inpa)):
        if float(inpa[i]) < float(lmin) :
            lmin = inpa[i]
            lind = []
            lind.append(i)
        else:
           if inpa[i] == lmin :
               lind.append(i)
    print('min =',lmin,'index =' ,lind)
        
inp = input("input numbers separated by ',': ")

min_array(inp)

# 4
print(10*'-','##4')

chart_len = int(input("len of chart"))

x = linspace(0, chart_len, 10000)
y = sin(x)*(1/(x/2))
figure(0, figsize = (10,7) )
plot(x, y)
show()

