class MyQueue(object): 

    def __init__(self):
        self.stack_in = []  # стек для добавления элементов
        self.stack_out = []  # стек для извлечения элементов
        

    def push(self, x):
        self.stack_in.append(x)  # добавляем элемент в стек входа
        

    def pop(self):
        if not self.stack_out:  # если стек выхода пуст
            while self.stack_in:  # переносим все элементы из stack_in
                self.stack_out.append(self.stack_in.pop())  # меняем порядок элементов
        
        return self.stack_out.pop()  # удаляем и возвращаем первый элемент очереди
        

    def peek(self):
        if not self.stack_out:  # если стек выхода пуст
            while self.stack_in:  # переносим элементы
                self.stack_out.append(self.stack_in.pop())  # инвертируем порядок
        
        return self.stack_out[-1]  # возвращаем первый элемент очереди
        

    def empty(self):
        return not self.stack_in and not self.stack_out  # очередь пуста, если оба стека пусты