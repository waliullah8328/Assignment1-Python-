# 2. Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration
#  print the sum of the current number and previous number
sum = 0
for i in range(10):
    print("current number = ",i)
    if i!=0:
        sum = sum + i
        print("current and previous num sum = ",sum)