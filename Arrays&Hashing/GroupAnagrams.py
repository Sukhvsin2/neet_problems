class Solution:
    # [ord(c) - ord('a')] will create a signature
    # count[signature] will help to push that string to the signature position
    # to create the list of string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # this will create signature
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)

        return result.values()