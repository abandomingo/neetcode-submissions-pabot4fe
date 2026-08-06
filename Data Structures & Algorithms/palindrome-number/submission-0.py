class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        if len(stringX) <= 1:
            return True
        
        end = -1
        
        # compare each string index usign two pointers
        for i in range(len(stringX)):
            if stringX[i] != stringX[end]:
                return False
            end -= 1
        
        # if we make it through and dont find any differences 
        return True