def sumoflist(nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum
def average(nums):
    s=0
    for i in nums:
        s=s+i
    return s/len(nums)
n=int(input("Enter the size of nums: "))
nums=list(map(int,input().strip().split()))
print("list is : ",nums)
print("Sum of list is : ",sumoflist(nums))
print("average of list is : ",average(nums))
