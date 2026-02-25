import heapq

class Solution(object):
    def lastStoneWeight(self, stones):

        heap = [-stone for stone in stones]
        heapq.heapify(heap) # Преобразуем в max-heap через отрицательные значения

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # самый тяжёлый
            x = -heapq.heappop(heap)  # второй по тяжести
            
            if y != x:
                heapq.heappush(heap, -(y - x))# Если веса разные - добавляем разницу обратно
        
        return -heap[0] if heap else 0 # Если остался один камень - вернуть его вес
        