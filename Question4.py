# 4. Accept number from user and calculate the sum of all number from 1 to a given number
n = int(input("Enter your last digit : "))

i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i+1
print(sum)
