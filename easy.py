"""x= [1,2,3]
y=x
y.append(4)
print(x)  # Output: [1, 2, 3, 4]"""

# 1st Debugging example
from threading import local


def add(a=[]): # bug , alternative: def add(a=None): if a is None: a = []
    a.append(1)
    return a

print(add())  # Output: [1]
print(add())  # Output: [1, 1]

# 2nd Debugging example
x=10 # here x is global variable
def test():
    print(x)  # Output: 10 , Accessing global variable x
    #`global x`, # use of global keyword will make x as global variable, so it will print 20
   # `local_x = local()` # if we use local() then x will be local variable, so it will print 10
    #`local_x.x = 20`
    #`print(local_x.x)` """ # Output: 20, here x as local variable, so it will not print 10
    x = 20 # unboundlocal error, because x is assigned a value inside the function, it is considered a local variable, but it is referenced before assignment

test()
