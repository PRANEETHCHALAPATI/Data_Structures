from collections import defaultdict
class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        fruitscount = defaultdict(int)
        n = len(arr)
        start = 0 
        max_length = 0
        for end in range(n):
            fruitscount[arr[end]] += 1 
            if len(fruitscount)>2:
                fruitscount[arr[start]] -= 1 
                if fruitscount[arr[start]]== 0:
                    del fruitscount[arr[start]]
                start += 1 
            max_length = max(max_length,end-start+1) 
        return max_length