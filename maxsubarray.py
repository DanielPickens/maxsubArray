class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
# array  = nums to find max_sum from nums sub array = {1, 2 3, 4}

        if not nums:
            return 0
        
        current_sum = 0
        max_sum = -sys.maxsize
        
        for n in nums:
            
            current_sum += n
            max_sum = max(current_sum, max_sum)
            
            if current_sum < 0:
                current_sum = 0
           
        return max_sum
      
    
    
    
    
    
    
    
    
  
    
