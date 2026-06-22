class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # num:index

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff], i]

            if val not in hashMap:  # for duplicate elements, only record the first time
                hashMap[val] = i

        return []

