class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""  
        for char in s:
            if char.isalnum():  
                string += char.lower()                  
        # n = len(string)
        # for i in range(n // 2):
        #     if string[i] != string[n - i - 1]:
        #         return False            
        # return True
        return string == string[::-1]
