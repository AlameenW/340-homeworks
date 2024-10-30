import numpy as np
a = [1,2,3,4]
c = [7,8,9]
b = tuple(zip(a,c))

def greet(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

# greet(name="Alice", age=30, city="New York")
def f1():
    print('Hello')

def f2(f):
    def wrapper(*args,**kwargs):
        print('started')
        val = f(*args,**kwargs)
        print('ended')
        return val
    return wrapper    

@f2
def f1(a):
    print('Hello')
# f1('Hi')

@f2
def sum(x,y):
    return(x+y)
# print(sum(2,3))

a = np.arange(15)
a = a.reshape(3,5)
print(a[0,4])

c =[[1,2],[3,4]]
print(c[0][1])