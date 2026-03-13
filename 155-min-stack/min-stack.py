class MinStack(object):  

    def __init__(self):
        self.stack = []  # основной стек 
        self.min_stack = []  # дополнительный стек для хранения текущих минимумов
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)  # добавляем элемент в основной стек
        
        if not self.min_stack or val <= self.min_stack[-1]:  # если стек минимумов пуст или новый элемент меньше текущего минимума
            self.min_stack.append(val)  # добавляем элемент в стек минимумов
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()  # удаляем верхний элемент из основного стека
        
        if val == self.min_stack[-1]:  # если удаляемый элемент равен текущему минимуму
            self.min_stack.pop()  # удаляем его из стека минимумов
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]  # возвращаем верхний элемент основного стека
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]  # возвращаем текущий минимальный элемент