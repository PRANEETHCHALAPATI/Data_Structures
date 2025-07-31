def maximum_sub_array(arr):
    if not arr:
        return 0 
    current_sum = arr[0] 
    max_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum += arr[i]
        current_sum = max(arr[i],current_sum)
        max_sum = max(max_sum, current_sum) 
    return max_sum 

def main():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    result = maximum_sub_array(arr)     
    print("Maximum subarray sum is:", result)
    
if __name__ == "__main__":
    main()
