def binary_search(arr,k):
    first = -1 
    last = -1 
    
    i = 0 
    j = len(arr) - 1
    while i<=j:
        mid = (i+j) // 2 
        if arr[mid] == k:
            last = mid 
            i = mid+1  
        elif arr[mid] < k:
            i = mid + 1
        else:
            j = mid - 1 
    return last 

def main(): 
    arr = list(map(int, input("Enter sorted array elements: ").split()))
    k = int(input("Enter the element to find the last occurrence of: "))
    result = binary_search(arr, k)
    if result != -1:
        print(f"The last occurrence of {k} is at index: {result}")  
    else:
        print(f"{k} is not present in the array.") 

if __name__ == "__main__":
    main()