def pattern(n):
    for i in range(1, n+1):
        if i%5==0:
            print('#', end='')
        else:
            print('*', end='')

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        pattern(n-i)
        print('')
