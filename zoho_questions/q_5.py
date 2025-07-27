def is_same(arr1, arr2):
    return arr1 == arr2

def find_number_of_operations(arr):
    n = len(arr)
    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid+1:][::-1]

    count = 0
    while not is_same(left_arr, right_arr):
        # Compare and decide which side to increment
        for i in range(mid):
            if left_arr[i] < right_arr[i]:
                left_arr[i] += 1
                break
            elif left_arr[i] > right_arr[i]:
                right_arr[i] += 1
                break
        count += 1
    return count

def main():
    print("Enter the array elements:")
    arr = list(map(int, input().split()))
    n = len(arr)

    if n == 1:
        print("The number of operations is: 0")
    else:
        mid = n // 2
        if is_same(arr[:mid], arr[mid+1:][::-1]):
            print("The number of operations is: 0")
        else:
            print("The number of operations is:", find_number_of_operations(arr))

main()
