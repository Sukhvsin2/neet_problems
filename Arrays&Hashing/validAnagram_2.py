class Solution(object):
    def isAnagram(self, s, t):
        '''
            sort the string and compare if all of the elements
            are at the same spots. 
            This is debatable because some sorting algorithms uses,
            O(n^2), O(nLogn), O(n), O(1).
        '''
        return sorted(s) == sorted(t)

        # inbuilt python DS which do the same thing as written at bottom. 
        return Counter(s) == Counter(t)

        '''
            check if the length of both strings are same or not,
            if not then it's not a valid anagram.

            created 2 hashmaps for both strings and then comparing,
            the occorance by iterating over the key values for both strings. 
        '''
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True
