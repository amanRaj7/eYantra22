for _ in range(int(input())):
    words = list(str(input()).split(' '))
    w_len = len(words)
    for i in range(w_len):
        if i==0:
            print(len(list(words[i]))-1, end = ',')
        elif i== (w_len-1):
            print((len(list(words[i]))))
        else:
            print(len(list(words[i])), end = ',')