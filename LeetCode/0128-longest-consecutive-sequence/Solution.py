class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        counter = 1
        maxCounter = 1
        if len(nums) == 0:
            return 0
        for number in numbers:
            if number-1 not in numbers:
                counter = 1
                for i in range(1,len(numbers)):
                    if number+i in numbers:
                        counter +=1
                    else:
                        if counter>maxCounter:
                            maxCounter = counter
                        break
        if counter>maxCounter:
            maxCounter = counter  
        return maxCounter