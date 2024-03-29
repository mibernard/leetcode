#leetcode premium problem
#works for strings containing no spaces
class Solution:
    def encode(self, strs: List[str]) -> str:
        return " ".join(strs)     
           
    def decode(self, s: str) -> List[str]:
        return s.split(" ")
        
#works for mostly all strings (using very uncommon delimiter: \x1c)
class Solution:
    def encode(self, strs: List[str]) -> str:
        # Using a delimiter that is less likely to appear in strings
        return '\x1c'.join(strs)  # '\x1c' is the File Separator in ASCII

    def decode(self, s: str) -> List[str]:
        return s.split('\x1c')


#works for 100% of strings
  class Solution:    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
