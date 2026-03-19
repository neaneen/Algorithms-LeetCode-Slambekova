class Solution(object):

    def intersection(self, nums1, nums2):
        
        set1 = set(nums1)  # делаем множество из первого массива
        result = set()     # множество для результата
        
        for num in nums2:  # проходим по второму массиву
            
            if num in set1:  # если элемент есть в первом массиве
                result.add(num)  # добавляем в результат
        
        return list(result)  # переводим в список
        
        