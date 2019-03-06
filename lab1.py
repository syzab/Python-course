# 1


xl = list(range(56,101,1))

for x in xl:
    y = 2*(x**2) + 2*x + 2
    print('y =',y,'| x =',x)

# 2 


f = int(input("factorial: "))

fac = 1
for i in range(1,f+1):
    fac = fac * i
print('factorial = ',fac)


# 3



#print(inpa)

def min_array(x):
    inpa = inp.split(',')
    lmin = inpa[0]
    for i in range (0,len(inpa)):
        #print(inpa[i],'  index:',i)
        if inpa[i] < lmin :
            lmin = inpa[i]
            lind = i
    print('min =',lmin,'index =' ,lind)
        
inp = input("input numbers separated by ',': ")


# 4

chart_len = int(input("len of chart"))

x = linspace(0, chart_len, 100)
y = sin(x)*(1/(x/2))
figure(0, figsize = (15,12) )
plot(x, y)
show()

