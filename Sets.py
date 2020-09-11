st = {1,2,6,"hii"}#declaring set
print(st)
#output {1, 2, 'hii', 6}

st.add(7)#Adds an element to the set
print(st)
#output {1, 2, 6, 7, 'hii'}

st.discard(6)#Remove the specified item
print(st)
#output {1, 2, 'hii', 7}

s1 = {1,2}
print(s1.issubset(st))#Returns whether another set contains this set or not
#output True

s = {5,8,7,9}
print(st.difference(s))#Returns a set containing the difference between two or more sets
#output {1, 2, 'hii'}

s.clear()#Removes all the elements from the set
#output {}

