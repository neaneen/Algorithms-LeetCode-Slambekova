class Solution(object):
    
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]  # сохраняем исходный цвет 
        if original_color == color:  # если исходный цвет совпадает с новым
            return image  #возвращаем исходное изображение
        
        rows, cols = len(image), len(image[0])  # размер изображения
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:  # если вышли за границы
                return  
            if image[r][c] != original_color:  # если цвет не соответствует исходному
                return  
            
            image[r][c] = color  # меняем цвет
            
            dfs(r + 1, c)  # идём вниз
            dfs(r - 1, c)  # идём вверх
            dfs(r, c + 1)  # вправо
            dfs(r, c - 1)  # влево
        
        dfs(sr, sc)  # запускаем заливку с начальной позиции
        return image  