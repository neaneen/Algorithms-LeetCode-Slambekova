class Solution(object):
    def sortArray(self, nums):

        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left_part = self.sortArray(nums[:middle])
        right_part = self.sortArray(nums[middle:])

        return self.merge(left_part, right_part)


    def merge(self, left_part, right_part):
        result = []
        i = 0
        j = 0

        while i < len(left_part) and j < len(right_part):

            if left_part[i] <= right_part[j]:
                result.append(left_part[i])
                i += 1
            else:
                result.append(right_part[j])
                j += 1

        while i < len(left_part):
            result.append(left_part[i])
            i += 1

        while j < len(right_part):
            result.append(right_part[j])
            j += 1
        return result
   