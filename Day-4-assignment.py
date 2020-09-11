  
for num in range(1,1000):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum = sum+ digit ** 3
       temp = temp/10
       break
 
   if num == sum:
       print(num)
