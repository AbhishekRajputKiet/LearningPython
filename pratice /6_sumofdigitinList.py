def sumOfDigitInList(nums):
    
    for i in nums:
        sum=0
        for digit in str(i):
            sum+=int(digit)
        print(sum,end=" ")
n=int(input("Enter the size of list: "))
nums=list(map(int,input().strip().split()))
# for i in range (0,n):
sumOfDigitInList(nums)   
print()
