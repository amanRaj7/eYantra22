# cook your dish here
def func(x):
    if(x==0):
        return x+3
    elif(x%2==0):
        return x*2
    else:
        return x*x

def print_arr(arr, n):
    for i in range(n):
        if(i==(n-1)):
            print(arr[i])
        else:
            print(arr[i], end=' ')
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(func, range(n)))
    print_arr(arr, n)
