def fabo(num):
    def fb(n):
        if n <= 0:
            print("Enter a valid number")
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return(fb(n-1)+fb(n-2))
        return num(n)
    return fb

@fabo
def fb_num(n):
    print(n,"this is the number")
print(fb_num(10))