# 1.Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum.
def summation(a, b):
    sum = a + b
    if(sum > 1000):
        return sum

    else:
     return "Sumation is below 1000"

print(summation(100, 1000))
print(summation(100, 100))



