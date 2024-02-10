class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord('a')] += 1
            if tuple(count) in strDict:
                strDict[tuple(count)] += [i]
            else:
                strDict[tuple(count)] = [i]
        
        return strDict.values()
            
        