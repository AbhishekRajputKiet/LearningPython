def largest(nums):
    maxi=-999999
    for i in nums:
        if i>maxi:
            maxi=i
    return maxi

def smallest(nums):
    mini=999999
    for i in nums:
        if i<mini:
            mini=i
    return mini

n=int(input("Enter the size of list: "))
nums=list(map(int,input().strip().split()))
print(largest(nums))
print(smallest(nums))
print(f"maximum of list is {largest(nums)} and minimum of list is {smallest(nums)}")
