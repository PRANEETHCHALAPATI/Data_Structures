class solution:
    def rotateArray(self, nums, x, y):
        #Write your code here...
        n = len(nums)
        x = x%n 
        y = y%n 
        nums[n-x:] = reversed(nums[n-x:])
        nums[:n-x] = reversed(nums[:n-x])
        nums[:] = reversed(nums[:])
        nums[:y] = reversed(nums[:y])
        nums[y:] = reversed(nums[y:])
        nums[:] = reversed(nums[:])
        return nums