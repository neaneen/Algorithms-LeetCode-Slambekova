import heapq  #библиотека приоритетной очереди
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}  #граф для узлов от 1 до n
        for u, v, w in times:  # проходим по всем рёбрам
            graph[u].append((v, w))  # добавляем соседа и время в список смежности
        
        dist = {i: float('inf') for i in range(1, n + 1)}  # массив минимальных времён
        dist[k] = 0  # время до стартового узла 0
        
        pq = [(0, k)]  # приоритетная очередь время,узел
        
        while pq:  
            time, node = heapq.heappop(pq)  # извлекаем узел с наименьшим временем
            
            if time > dist[node]: #нашли худший путь
                continue  
            
            for neighbor, weight in graph[node]:  
                new_time = time + weight  # новое время до соседа
                if new_time < dist[neighbor]:  # если нашли короткий путь
                    dist[neighbor] = new_time  # обновляем минимальное время
                    heapq.heappush(pq, (new_time, neighbor))  # добавляем соседа в очередь
        
        max_time = max(dist.values())  # находим максимальное время
        
        return max_time if max_time != float('inf') else -1  # если есть недостижимые узлы, возвращаем -1