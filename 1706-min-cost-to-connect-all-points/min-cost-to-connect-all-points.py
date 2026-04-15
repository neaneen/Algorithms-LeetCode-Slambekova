class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        in_mst = [False] * n  # массив, включена ли точка в дерево
        min_dist = [float('inf')] * n  # мин.расст. 
        min_dist[0] = 0  
        result = 0  # вес 

        for _ in range(n):  
            u = -1  # индекс текущей вершины

            for i in range(n): 
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]) :
                    u = i  # обновляем вершину с мин.раст.

            in_mst[u] = True  # включаем вершину в дерево
            result += min_dist[u]  # добавляем её вес к результату

            for v in range(n):  # обновляем расст. до остальных вершин
                if not in_mst[v]:  # только непосещённые вершины
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])  # манхэттенское расстояние
                    if dist < min_dist[v]:
                        min_dist[v] = dist  

        return result  
        