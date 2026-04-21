class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)  # сумма элементов

        if total % 2 != 0:
            return False  # нельзя разделить

        target = total // 2  # половина суммы

        dp = [False] * (target + 1)  # достижимость сумм
        dp[0] = True  #0 можно собрать

        for num in nums: 
            for i in range(target, num - 1, -1):  #справа налево
                if dp[i - num]:
                    dp[i] = True  # можно собрать сумму i

        return dp[target]  #достижима ли половина
        