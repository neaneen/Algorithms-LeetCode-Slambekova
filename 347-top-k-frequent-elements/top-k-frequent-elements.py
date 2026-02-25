from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)# Подсчитываем частоту каждого числа
        
        heap = []# Используем min-heap размером k
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]# Возвращаем только элементы без частот