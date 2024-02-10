class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter_freq = {}
        for char in s:
            counter_freq[char] = counter_freq.get(char, 0) + 1
        
        sorted_counter = sorted(counter_freq.keys(), key=lambda x: counter_freq[x], reverse=True)
        
        sorted_string = ''
        for char in sorted_counter:
            sorted_string += char * counter_freq[char]
        
            
        return sorted_string