import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            # Поддерживаем размер кучи равным k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Корень кучи - k-й наибольший элемент
        return heap[0]