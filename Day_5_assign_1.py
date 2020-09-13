Lista = [1,1,5]
Listb = [1,5,6,4,1,2,3,5]
def subList(a,b):
    if set(a).issubset(set(b)):
        print("Its a match")
    else:
        print("Its gone")

x = subList(set(Lista),set(Listb))