class Solution(object):
    def deleteNode(self, root, key):

        if not root:
            return None
        
        if key < root.val: # Если ключ меньше значения корня, идём в лево
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:  # Если ключ больше значения корня, идём в правое
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not root.left: # у узла нет левого ребенка
                return root.right  # Возвращаем правого ребенка 
            
            if not root.right: # у узла нет правого ребенка
                return root.left # возвращаем левого
            
            # у узла есть оба ребенка
            min_node = root.right # Находим минимальный узел в правом поддереве
            while min_node.left:  # Идём максимально влево
                min_node = min_node.left
            
            # Заменяем значение текущего узла на значение минимального узла
            root.val = min_node.val
            
            # Удаляем минимальный узел из правого поддерева
            root.right = self.deleteNode(root.right, min_node.val)
        
        # Возвращаем корень 
        return root
        