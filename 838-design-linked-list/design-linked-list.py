class Node(object):  # класс узла списка
    
    def __init__(self, val=0, next=None):
        self.val = val  # значение узла
        self.next = next  # ссылка на следующий узел


class MyLinkedList(object):  # объявление класса связного списка

    def __init__(self):
        self.head = None  # указатель на первый элемент списка
        self.size = 0  # текущее количество элементов
        

    def get(self, index):
        if index < 0 or index >= self.size:  # проверка корректности индекса
            return -1  # если индекс некорректен
        
        curr = self.head  # начинаем с первого элемента
        
        for i in range(index):  # двигаемся по списку до нужного индекса
            curr = curr.next  # переходим к следующему узлу
        
        return curr.val  # возвращаем значение найденного узла
        

    def addAtHead(self, val):
        new_node = Node(val)  # создаем новый узел
        new_node.next = self.head  # новый узел указывает на старую голову
        self.head = new_node  # обновляем голову списка
        self.size += 1  # увеличиваем размер списка
        

    def addAtTail(self, val):
        new_node = Node(val)  # создаем новый узел
        
        if not self.head:  # если список пуст
            self.head = new_node  # новый узел становится головой
        else:
            curr = self.head  # начинаем обход списка
            
            while curr.next:  # идем до последнего узла
                curr = curr.next
            
            curr.next = new_node  # добавляем новый узел в конец
        
        self.size += 1  # увеличиваем размер списка
        

    def addAtIndex(self, index, val):
        if index > self.size:  # если индекс больше длины списка
            return  # вставка невозможна
        
        if index <= 0:  # если индекс 0 или меньше
            self.addAtHead(val)  # добавляем в начало
            return
        
        if index == self.size:  # если индекс равен длине списка
            self.addAtTail(val)  # добавляем в конец
            return
        
        curr = self.head  # начинаем обход
        
        for i in range(index - 1):  # доходим до узла перед нужным индексом
            curr = curr.next
        
        new_node = Node(val)  # создаем новый узел
        new_node.next = curr.next  # связываем новый узел со следующим
        curr.next = new_node  # связываем предыдущий узел с новым
        
        self.size += 1  # увеличиваем размер списка
        

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:  # проверка корректности индекса
            return  # удаление невозможно
        
        if index == 0:  # если удаляем первый элемент
            self.head = self.head.next  # сдвигаем голову списка
        else:
            curr = self.head  # начинаем обход
            
            for i in range(index - 1):  # доходим до узла перед удаляемым
                curr = curr.next
            
            curr.next = curr.next.next  # пропускаем удаляемый узел
        
        self.size -= 1  # уменьшаем размер списка