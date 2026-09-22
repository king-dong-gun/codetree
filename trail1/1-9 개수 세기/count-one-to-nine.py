n = int(input())
number = list(map(int, input().split()))
arr = [1,2,3,4,5,6,7,8,9]

for i in range(1,10):
    count = 0
    for j in number:
        if j  == i:
            count += 1
    print(count)