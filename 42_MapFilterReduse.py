
# MAP
def cube(x):
    return x*x*x
print(cube(3))



l=[2,4,5,1,6]
# newl=[]
# for i in l:
#     newl.append(cube(i))

newl = list(map(cube,l))
print(newl)

#  FILTER
def filter_function(a):
    return a>2
newlist = list(filter(filter_function,l))
print(newlist)

# REDUCE

from functools import reduce
num = [1 ,3,4,5,6]
def mysum(x,y):
    return x+y
sum = reduce(mysum,num)
print(sum) 

