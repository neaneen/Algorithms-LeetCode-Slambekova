class Solution(object):
    def nextGreatestLetter(self, letters, target):
    
        left = 0
        right = len (letters) - 1

        while left <= right:
            center = (left + right) //2
            current = letters [center]

            if current > target:
                right = center - 1
            else:
                left = center + 1
        if left <len (letters):
            return letters [left]
        else: 
            return letters[0]       