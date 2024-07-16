def print_arr(arr):
    for i in arr:
        print(i, end=' ')
    print('')
for _ in range(int(input())):
    a, d, n = [int(x) for x in input().split()]
    arr = [a+i*d for i in range(n)]
    square_arr = [x**2 for x in arr]
    print_arr(arr)
    print_arr(square_arr)
    print(sum(square_arr))