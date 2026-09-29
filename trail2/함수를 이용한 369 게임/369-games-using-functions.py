a, b = map(int, input().split())

# Please write your code here.

def check_num(n):
    if n % 3 == 0:
        return True

    for digit in str(n):
        if digit == '3' or digit == '6' or digit == '9':
            return True
    return False


count = 0

for i in range(a, b + 1):
    if check_num(i):
        count += 1

print(count)