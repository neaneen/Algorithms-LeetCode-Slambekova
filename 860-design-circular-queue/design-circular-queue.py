class MyCircularQueue(object):  

    def __init__(self, k):
        self.queue = [0] * k  # создаем массив фиксированного размера k
        self.size = k  # максимальный размер очереди
        self.front = 0  # индекс начала очереди
        self.rear = -1  # индекс конца очереди
        self.count = 0  # текущее количество элементов в очереди
        

    def enQueue(self, value):
        if self.isFull():  # если очередь заполнена
            return False  # добавление невозможно
        
        self.rear = (self.rear + 1) % self.size  # сдвигаем указатель конца по кругу
        self.queue[self.rear] = value  # записываем элемент в очередь
        self.count += 1  # увеличиваем количество элементов
        
        return True  
        

    def deQueue(self):
        if self.isEmpty():  # если очередь пуста
            return False  # удаление невозможно
        
        self.front = (self.front + 1) % self.size  # сдвигаем указатель начала по кругу
        self.count -= 1  # уменьшаем количество элементов
        
        return True  
        

    def Front(self):
     
        if self.isEmpty():  # если очередь пуста
            return -1  # возвращаем -1
        
        return self.queue[self.front]  # возвращаем первый элемент
        

    def Rear(self):
        if self.isEmpty():  # если очередь пуста
            return -1  # возвращаем -1
        
        return self.queue[self.rear]  # возвращаем последний элемент
        

    def isEmpty(self):
        return self.count == 0  # очередь пуста, если элементов нет
        

    def isFull(self):
        return self.count == self.size  # очередь заполнена, если достигнут максимальный размер