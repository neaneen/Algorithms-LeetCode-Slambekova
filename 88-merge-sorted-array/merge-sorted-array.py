class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index1 = m - 1
        index2 = n - 1
        merge_position = m + n - 1

        while index1 >= 0 and index2 >= 0:

            if nums1[index1] > nums2[index2]:
                nums1[merge_position] = nums1[index1]
                index1 -= 1
            else:
                nums1[merge_position] = nums2[index2]
                index2 -= 1
            merge_position -= 1

        while index2 >= 0:
            nums1[merge_position] = nums2[index2]
            index2 -= 1
            merge_position -= 1
 