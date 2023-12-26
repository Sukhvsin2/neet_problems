class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1:
            return nums

        count = {}
        # this will create an empty len(n+1) size of list. 
        freq = [[] for i in range(len(nums) + 1)]

        # will increase the count in the dictonary
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # arrange the dictonary values in the empty array,
        # [1,1,1,2,2,3] -->
        # [_,[3],[2],[1]]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # read the array from back to get the most freq value. 
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
            if len(res) == k:
                return res
        
