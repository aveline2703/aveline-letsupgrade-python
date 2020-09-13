def primeNumber(num):
    for i in range(2,num):
        if num%2 == 0:
            break
        else:
            return num
lst = list(range(1,2500))
a = filter(primeNumber,lst)
print(list(a))
