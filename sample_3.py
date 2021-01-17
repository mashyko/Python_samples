# definition of function
def change(y):
    y[1]=4
x=[1,2,3]
change(x)
print (x)

# Fibonachi sseries
def fib(n):
    a,b=0,1
    while b < n:
     print (b,)
     a,b=b,a+b
print ("Fibonachi number :")
fib(2000)
