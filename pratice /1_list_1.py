
def intractwithfirstandlast(nums,n):
    nums[0],nums[n-1]=nums[n-1],nums[0]
    return nums

# swap of first and last element of the list 
nums = [12, 35, 9, 56, 24]
n=5
print(intractwithfirstandlast(nums,n))

