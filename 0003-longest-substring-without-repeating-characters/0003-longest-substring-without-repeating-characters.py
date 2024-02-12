class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0 if len(s) == 0 else 1
        curX, curY = 0, 1
        
        while curY < len(s):
            if s[curY] not in s[curX:curY]:
                curY += 1
                answer = max(curY-curX, answer)
            else:
                answer = max(curY-curX, answer)
                curX += 1
                curY = curX + 1
        
        return answer