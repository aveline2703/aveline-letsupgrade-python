print("Enter x to stop")
print("Enter range:")
start = input()
if start == 'x':
    exit()
else:
    end = input()
    lower = int(start)
    upper = int(end)
    for num in range(lower,upper+1):
        total = 0
        temp = num
        while temp != 0:
            digit = temp % 10
            total += digit**3
            temp //= 10
        if num == total:
            print(num)
