import math


def compute_distance(x1, y1, x2, y2):

    distance = 0

    distance = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    print("Distance: ",end='')
    print("%.2f" % distance)



if __name__ == '__main__':
    

    test_cases = int(input())
    
    for _ in range(test_cases):
    
        l = list(map(int,input().split()))
    
        x1, y1, x2, y2=l[0], l[1], l[2], l[3]
        compute_distance(x1, y1, x2, y2)
