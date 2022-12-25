#build a function to get the right result of multiplication or sum
def mult_or_sum(a, b):
    if a*b >= 1000: 
        return a+b
    else:
        return a*b

given1 = mult_or_sum(20,30)
print("The result is", given1)

given2 = mult_or_sum(30,40)
print("The result is", given2)