file = open('Ranjan.txt','r')
try:
    file.write("hlo")
    file.close()
except Exception as e:
    print(e)
print(file.read())

#output not writable
#       Hi
