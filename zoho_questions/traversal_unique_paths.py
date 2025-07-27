list = []
def traverse(arr,i,j,str,n):
    if i == n-1 and j == n-1:
        if str+arr[i][j] not in list:
            list.append(str+arr[i][j])
        return 
    elif i >= n or j >= n:
        return
    else:
        traverse(arr,i+1,j,str+arr[i][j],n)
        traverse(arr,i,j+1,str+arr[i][j],n)  

def is_palindrome(s):
    return s == s[::-1]
    
def main():
    n = int(input("Enter the size of the matrix: "))
    arr =[] 
    for i in range(n):
        print(f"Enter row {i+1} elements separated by space:")
        row = input().split()
        arr.append(row) 
    traverse(arr,0,0,"",n)
    print(len(list))
    for i in list:
        if is_palindrome(i):
            print(i) 

if __name__ == "__main__":   
    main()