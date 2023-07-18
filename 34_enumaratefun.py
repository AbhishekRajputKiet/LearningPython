nums = [89,4,2,43,23,67,1]
# index=0
# for index in nums :
#     print(index)
#     if index==3:
#         print("Abhishek")
#     index=index +1

# enumerate function give value with index
# enumerate can use on untrack the value of taples


# for index ,num in enumerate(nums) :
#     print(num)
#     if index==3:
#         print("Abhishek")

# for index in enumerate(nums) :
#     print(index)
#     if index==3:
#         print("Abhishek")


for index ,num in enumerate(nums,start=1) :
    print(num)
    if index==3:
        print("Abhishek")
