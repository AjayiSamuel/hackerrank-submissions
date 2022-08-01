from typing import List


# class Solution:
#     def __init__(self, nums ):
def twoSum(nums: List[int], target: int) -> List[int]:
    for i,j in enumerate(nums):
        for k,l in enumerate(nums):
            if i == k:
                pass
            elif j + l == target:
                return [i,k]


print(twoSum(nums=[2,7,11,15], target=9))

# hashmap = {}
#     for i in range(len(nums)):
#         hashmap[nums[i]] = i
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [hashmap[complement], i]

# hashmap = {}
# for i in range(len(nums)):
#     complement = target - nums[i]
#     if complement in hashmap:
#         return [i, hashmap[complement]]
#     hashmap[nums[i]] = i
