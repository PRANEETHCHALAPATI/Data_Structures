class solution:
    def findKthMergedElement(self, list1, list2, k):
        #Write your code here...
        list1.extend(list2)
        list1.sort()
        return list1[k-1]