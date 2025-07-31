def binary_search(arr,x):
    i = 0
    j = len(arr) - 1 
    while i<=j:
        mid = (i+j)//2 
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            i = mid+1 
        else:
            j = mid -1 
    return -1  

def main():
    arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))
    x = int(input("Enter the element to search for: "))
    result = binary_search(arr, x)
    if result != -1:
        print(f"Element found at index: {result}")      
    else:
        print("Element not found in the array.") 

if __name__ == "__main__":
    main()
