
# nums=[]
# n=int(input("Enter a size of list : "))
# for i in range(0,n):
#     p=int(input())
#     nums.append(p)
# counting function 

def count(arr,b):
    c=0
    for i in arr:
        if i==b:
            c+=1
    return c



a=int(input("Enter a input : "))
arr=list(map(int,input().strip().split())) 
b=int(input("Count the occurence of : "))
print(count(arr,b))
print(arr.count(b))

