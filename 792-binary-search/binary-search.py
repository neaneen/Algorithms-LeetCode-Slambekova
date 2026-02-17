class Solution(object):
    def search(self, n, target):
        
        left_border = 0
        right_border = len(n) - 1
        
        while left_border <= right_border:
            
            center = (left_border + right_border) // 2
            current = n[center]
            
            if current == target:
                return center
            
            if target > current:
                left_border = center + 1
            else:
                right_border = center - 1
        
        return -1
