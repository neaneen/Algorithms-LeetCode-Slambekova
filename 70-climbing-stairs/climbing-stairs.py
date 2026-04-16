class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1 

        p2 = 1  
        p1 = 2  

        for i in range(3, n + 1):  
            current = p2 + p1 
            p2 = p1 
            p1 = current  

        return p1  
       


    
        