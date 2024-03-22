class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(s)
        list2 = sorted(t)

        if list1 == list2:
            return True
