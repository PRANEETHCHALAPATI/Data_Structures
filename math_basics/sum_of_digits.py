class solution:
    def sumOfDigits(self, num):
        #Write your code here...
        x = num%9 
        if x == 0:
            return 9 
        else:
            return x