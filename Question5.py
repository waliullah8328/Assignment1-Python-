# 5. Given a list, iterate it, and display numbers divisible by five,
# and if you find a number greater than 150, stop the loop iteration.
l = [10,20,30,40,47,50,53,100,150,110,350,370,400]
for i in l:
    if i < 150:
        if i%5 == 0:
            print(i)
    else:
     break