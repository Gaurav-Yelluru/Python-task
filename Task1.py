#Factorial using non-tail recursion

def fact_non_tail(n):
    if(n<2):
        return 1
    else:
        return n*fact_non_tail(n-1)
    
n=int(input('Enter a number for factorial using non-tail recursion: '))
f=fact_non_tail(n)
print(f'Factorial of {n} is {f}')

##Factorial using tail recursion

def factTR(n,x):
    if (n==0):
        return x
    else:
        return factTR(n-1,n*x)
    
def fact_tail(n):
    return factTR(n,1)

n=int(input('Enter a number for factorial using tail recursion: '))
f=fact_tail(n)
print(f'Factorial of {n} is {f}')

#exponent using non-tail recursion

def power_non_tail(a,n):
    if(n==0):
        return 1
    else:
        return a*power_non_tail(a,n-1)
    
a=int(input('Enter a number to find power using non-tail recursion: '))
n=int(input('Enter the degree: '))
p=power_non_tail(a,n)
print(f'{a} to the power of {n} is {p}')

#exponent using tail recursion

def powerTR(a,n,m):
    if(n==0):
        return m
    else:
        return powerTR(a,n-1,m*a)
    
def power_tail(a,n):
    return powerTR(a,n,1)
    
a=int(input('Enter a number to find power using tail recursion: '))
n=int(input('Enter the degree: '))
p=power_tail(a,n)
print(f'{a} to the power of {n} is {p}')