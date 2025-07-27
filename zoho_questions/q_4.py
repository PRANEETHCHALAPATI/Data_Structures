listx = [] 
def find_max_sub_array(matrix,i,j,k,n):
    if i >= n or j >= n or i+k-1 >= n or j+k-1 >= n:
        return 
    else:
        total_sum = 0
        for x in range(i,i+k):
            total_sum += sum(matrix[x][j:j+k])
        listx.append([total_sum,i,j])
        find_max_sub_array(matrix,i+1,j,k,n)
        find_max_sub_array(matrix,i,j+1,k,n) 
def print_max_sub_array(matrix,listx,k):
    temp = list(map(lambda x:x[0],listx))
    max_sum = max(temp)
    final_sub_array = list(filter(lambda x:x[0]==max_sum ,listx)) 
    i = final_sub_array[0][1]
    j = final_sub_array[0][2] 
    print("the maximum sub array is\n")
    for x in range(i,i+k):
        for y in range(j,j+k):
            print(matrix[x][y],end="  ")
        print() 
    print("the maximum sum is :\n")
    print(final_sub_array[0][0])
def main():
    n = int(input("Enter the size of matrix:\n"))
    k = int(input("Enter the size of sub_array:\n"))
    matrix =[] 
    for i in range(n):
        temp = list(map(int,input().split())) 
        matrix.append(temp) 
    find_max_sub_array(matrix,0,0,k,n)
    print_max_sub_array(matrix,listx,k)
main()    
        