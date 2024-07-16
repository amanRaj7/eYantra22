# cook your dish here
def print_arr(arr):
    for i in arr:
        print(i, end=' ')
    print('')

for _ in range(int(input())):
    len = int(input())
    arr = list(int(x) for x in input().split())
    print_arr(arr[::-1])
    arr3 = []
    arr5 = []
    for i in range(len):
        if i%3==0 and i!=0:
            arr3.append(arr[i]+3)
        if i%5==0 and i!=0:
            arr5.append(arr[i]-7)
    print_arr(arr3)
    print_arr(arr5)
    print(sum(arr[3:8]))