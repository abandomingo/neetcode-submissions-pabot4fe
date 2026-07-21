class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        ans = nums + nums
        return ans