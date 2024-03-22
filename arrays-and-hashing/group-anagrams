class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1
            
            result[tuple(count)].append(s) #tuple to make the list keyable
        return result.values()

#time: O(m*n) 
