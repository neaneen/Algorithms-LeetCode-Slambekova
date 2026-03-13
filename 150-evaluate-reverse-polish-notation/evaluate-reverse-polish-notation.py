class Solution(object):  
    
    def evalRPN(self, tokens):
      
        
        stack = []  # стек
        
        for token in tokens:  

            if token == "+":  # операция сложения
                b = stack.pop()  # второй операнд
                a = stack.pop()  # первый операнд
                stack.append(a + b)  # добавляем результат в стек

            elif token == "-":  # операция вычитания
                b = stack.pop()  # второй операнд
                a = stack.pop()  # первый операнд
                stack.append(a - b)  # добавляем результат

            elif token == "*":  # операция умножения
                b = stack.pop()  # второй операнд
                a = stack.pop()  # первый операнд
                stack.append(a * b)  # добавляем результат

            elif token == "/":  # операция деления
                b = stack.pop()  # второй операнд
                a = stack.pop()  # первый операнд
                stack.append(int(float(a) / b))  # деление с усечением к нулю

            else: 
                stack.append(int(token))  

        return stack[0]  