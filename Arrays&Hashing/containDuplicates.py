class Solution:
    # sort & iterate
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None

        for n in nums:
            if prev == n:
                return True
            prev = n

        return False
    
class Solution:
    # create a hash map
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = dict.fromkeys(nums, 0)
        for n in nums:
            res[n] += 1
            if res[n] > 1:
                return True

        return False

class Solution:
    # create a set of an array & compare with original array
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        if len(res) != len(nums):
            return True

        return False