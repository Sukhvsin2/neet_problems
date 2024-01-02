class Solution(object):
    def containsDuplicate(self, nums):
        ''' convert array into set to delete all duplicates,
            compare the length of the array with set.
            If not equal then True or False.
        '''
        return not len(nums) == len(set(nums))
        
