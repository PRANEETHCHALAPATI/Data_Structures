class solution:
    def findDuplicate(self, nums):
        #Write your code here...
        return sum(nums)-len(nums)*(len(nums)-1)//2 
