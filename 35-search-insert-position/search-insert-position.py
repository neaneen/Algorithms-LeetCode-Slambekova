class Solution(object):
    def searchInsert(self, n, target):
        left = 0
        right = len (n) - 1

        while left <= right:
            center = (left + right) // 2
            current = n[center]

            if current == target:
                return center
            if target > current:
                left = center + 1
            else:
                right = center - 1
        return left
        