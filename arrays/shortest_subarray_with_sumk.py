class solution:
    def shortestSubarrayWithSumK(self, arr, n, k):
        from collections import defaultdict 
        prefix_sum = 0
        min_len = n+1
        sum_dict = defaultdict(int) 
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum == k:
                if min_len>i+1:
                    min_len = i+1 
            if prefix_sum-k in sum_dict:
                curr_len = i-sum_dict[prefix_sum-k]
                if min_len>curr_len:
                    min_len = curr_len  
            if prefix_sum not in sum_dict:
                sum_dict[prefix_sum] = i 
        if min_len == n+1:
            return -1 
        else:
            return min_len 
