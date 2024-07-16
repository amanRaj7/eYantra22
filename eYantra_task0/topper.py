def print_arr(x):
    for i in x:
        print(i[0], end=' ')
    print('')

for _ in range(int(input())):
    len = int(input())
    arr_names = []
    max = 0
    for i in range(len):
        stud = list(input().split())
        stud[1] = float(stud[1])
        arr_names.append(stud)
        if max<=stud[1]:
            max = stud[1]
    topper = sorted(list(filter(lambda x: x[1]==max, arr_names)))
    print_arr(topper)
    