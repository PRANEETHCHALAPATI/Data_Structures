class solution:
    def getCommonElements(self, nums1, nums2, nums3):
        #Write your code here...
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = len(nums3)
        i = 0 
        j = 0
        k = 0
        ans = []
        while i < n1 and j < n2 and k < n3:
            if nums1[i] == nums2[j] == nums3[k]:
                ans.append(nums1[i])
                i += 1 
                j += 1 
                k += 1 
            else:
                min_value = min(nums1[i],nums2[j],nums3[k]) 
                if nums1[i] == min_value:
                    i += 1 
                if nums2[j] == min_value:
                    j += 1 
                if nums3[k] == min_value:
                    k += 1
        return ans
                
    
    