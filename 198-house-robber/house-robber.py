class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0  

        if len(nums) == 1:
            return nums[0]  

        p2 = 0  
        p1 = 0  

        for money in nums:
            current = max(p1, p2 + money)  
            p2 = p1  
            p1 = current  

        return p1  
        
        