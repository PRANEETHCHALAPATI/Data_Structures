class solution:
    def longestSubarrayWithSumK(self, arr, n, k):
       from collections import defaultdict
       sum_dict = defaultdict(int)
       prefix_sum = 0 
       max_len = 0
       for i in range(n):
           prefix_sum += arr[i]
           if prefix_sum == k:
               max_len = i+1 
           if (prefix_sum-k) in sum_dict:
               curr_len = i-sum_dict[prefix_sum-k] 
               if curr_len> max_len:
                   max_len = curr_len 
           if prefix_sum not in sum_dict :
               sum_dict[prefix_sum] = i 
       return max_len 
               
    
     
