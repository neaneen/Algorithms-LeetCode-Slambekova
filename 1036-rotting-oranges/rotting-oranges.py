from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0]) 
        queue = deque()  # очередь для BFS
        fresh_count = 0  # счётчик свежих апельсинов
        
        for r in range(rows):  
            for c in range(cols):  
                if grid[r][c] == 2:  # если гнилой
                    queue.append((r, c, 0))  # добавляем в очередь
                elif grid[r][c] == 1:  # если свежий 
                    fresh_count += 1  # + счётчик свежих
        
        if fresh_count == 0:  # если свежих нет
            return 0  # 0 минут
        
        minutes = 0  # хранение прошедшего времени
        
        while queue:  
            r, c, time = queue.popleft()  # извлекаем координаты и время
            minutes = max(minutes, time)  # обновляем максимальное время
            
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4 направления
                nr, nc = r + dr, c + dc  #координаты соседнего
                if 0 <= nr < rows and 0 <= nc < cols:  # если в границах
                    if grid[nr][nc] == 1:  # если сосед - свежий апельсин
                        grid[nr][nc] = 2  # делаем гнилым
                        fresh_count -= 1  # - счётчик свежих
                        queue.append((nr, nc, time + 1))  # добавляем в очередь с увеличенным временем
        
        return minutes if fresh_count == 0 else -1  # если все свежие заражены, возвращаем время, иначе -1
        