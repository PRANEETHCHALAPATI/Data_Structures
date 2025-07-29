class solution:
    def longestSubarrayWithSumK(self, arr, n, k):
        sliding_sum = arr[0] 
        max_len = 0 
        i = 0 
        j = 0 
        while j<n:
            if sliding_sum == k:
                max_len = max(max_len, j - i + 1)
                j += 1 
                if j<n:
                    sliding_sum += arr[j]
            elif sliding_sum<k:
                j += 1 
                if j< n:
                    sliding_sum += arr[j] 
            else:
                if i == j:
                    i += 1 
                    j += 1 
                    if j < n:
                        sliding_sum = arr[j]
                else:
                    sliding_sum -= arr[i]
                    i+= 1 
        return max_len
    
     
