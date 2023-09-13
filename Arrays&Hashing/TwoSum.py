class Solution:
    # n^2 approach where target - element = res and if res exist in the 
    # array return the index for [element, res].
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        res = 0
        output = list()
        for i in range(len(nums)):
            res = target - nums[i]
            for j in range(i+1, len(nums)):
                if res == nums[j]:
                    output.append(i)
                    output.append(j)
        return output
        
class Solution:
    # Store prev[number] = index and then target - element = diff
    # now if diff exists in prev then return prev[diff] --> this will give index of the 
    # element
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prev:
                return [prev[diff], index]
            prev[number] = index