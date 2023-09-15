
# def double(x):
#     return x*2
def fun1(fun2,val):
    return 6+fun2(val)

double =lambda x :x*2
cube =lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/3
print(double(5))
print(cube(2))
print(avg(2,3,4))
print(fun1(cube,3))