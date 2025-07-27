def find_missing_number(arr,n):
    i = 0 
    j = 1
    difference = int((arr[n-1]-arr[0])/n)
    while i<n and j<n:
        if arr[j]-arr[i] == difference:
            i += 1  
            j += 1 
        else:
            print(arr[i]+difference)
            return 
def main():
    n = int(input())
    arr = list(map(int,input().split())) 
    find_missing_number(arr,n)
main()