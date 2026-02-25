import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        # Инициализируем кучу первыми элементами
        for num in nums:
            self.add(num)

    def add(self, val):
        
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # Корень кучи - текущий k-й наибольший
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)