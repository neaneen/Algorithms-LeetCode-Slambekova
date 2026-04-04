class Solution(object):
    def numIslands(self, grid):
        if not grid:  # если пусто
            return 0  
        
        rows, cols = len(grid), len(grid[0])  # размеры 
        count = 0  # счётчик 
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:  # если вышли за границы
                return  
            if grid[r][c] != '1':  # если текущая клетка не суша 
                return  
            
            grid[r][c] = '0'  # помечаем как посещенную 
            dfs(r + 1, c)  # вниз
            dfs(r - 1, c)  # вверх
            dfs(r, c + 1)  # вправо
            dfs(r, c - 1)  # влево
        
        for r in range(rows):  
            for c in range(cols):  
                if grid[r][c] == '1':  # если нашли сушу
                    count += 1  # увеличиваем счётчик 
                    dfs(r, c)  # запускаем заливку
        return count  
        