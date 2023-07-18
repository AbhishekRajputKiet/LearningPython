def swap(nums,pos1,pos2):
    nums[pos1]=nums[pos2]
    return nums
nums=[23, 65, 19, 90]
pos1=2
pos2=3
print(swap(nums,pos1,pos2))