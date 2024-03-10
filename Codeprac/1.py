# # L = [int(x) for x in input().split()]
# from re import split

# # N = input()
# # M = N.split()
# # L = [int(x) for x in input().split()]
# # print(L)
# # input_string = input()
# # print(input_string, type(input_string))
# # input_list = input_string.split()
# # print(input_list, type(input_list))

# x, y = map(int, input().split())
# print(x, y)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
            if nums[i] + nums[i+1]==target:
                 return l = [i ,i+1]
