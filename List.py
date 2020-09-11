Lst = ["Aveline",1,2,3,4]#declaring list
print(Lst)
#output ['Aveline', 1, 2, 3, 4]

Lst.append("Aveline")#Adding item to the last of the list
print(Lst)
#output ['Aveline', 1, 2, 3, 4, 'Aveline']

lst = Lst.copy()#copying list items to another variable
print(lst)
#output ['Aveline', 1, 2, 3, 4, 'Aveline']

lst.pop(0)#poping out item from the list at the index 0
print(lst)
#output [1, 2, 3, 4, 'Aveline']

lst.reverse()#reversing the list items
print(lst)
#output ['Aveline', 4, 3, 2, 1]

lst.clear()#Clearing entire list items
print(lst)
#output []
