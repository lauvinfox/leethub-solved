class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointerL = 0
        pointerR = len(height) - 1
        
        maxAmountWater = 0
        
        while pointerL < pointerR:
            amountWater = min(height[pointerL], height[pointerR]) * (pointerR - pointerL)
            maxAmountWater = max(maxAmountWater, amountWater)
            
            if height[pointerL] < height[pointerR]:
                pointerL += 1
            else:
                pointerR -= 1
        
        return maxAmountWater
        
            
        