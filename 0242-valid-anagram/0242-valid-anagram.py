class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        checklist = [0] * 26
        for c in s:
            checklist[ord(c) - ord('a')] += 1
            checklist1 = checklist 

        checklist = [0] * 26
        for c in t:
            checklist[ord(c) - ord('a')] += 1
            checklist2 = checklist
        
        if tuple(checklist1) == tuple(checklist2):
            return True
        else:
            return False
            
        