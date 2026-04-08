class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0
        currentConsecutive = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                currentConsecutive += 1
            else:
                currentConsecutive = 0 

            if maxConsecutiveOnes < currentConsecutive:
                maxConsecutiveOnes = currentConsecutive

        return maxConsecutiveOnes

        
             
                


        