from collections import defaultdict

class Solution(object):

    def groupAnagrams(self, strs):
        
        anagrams = defaultdict(list)  
        
        for word in strs:
            
            key = ''.join(sorted(word))  # сортируем буквы в слове, получаем ключ
            
            anagrams[key].append(word) # добавляем слово в группу по ключу
        
        return list(anagrams.values()) # возвращаем все группы анаграмм
       
        