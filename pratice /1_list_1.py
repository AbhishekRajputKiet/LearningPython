
def intractwithfirstandlast(nums,n):
    nums[0]=nums[n-1]
    return nums



nums = [12, 35, 9, 56, 24]
n=5
print(intractwithfirstandlast(nums,n))

