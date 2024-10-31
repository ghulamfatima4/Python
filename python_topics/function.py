#function to calculate sum  of 2 values
def sum(a,b):
    sum = a + b
    print(sum)

sum(10, 20)

#function to calculate print and sum 2 values 
def two_num(x,y=50):
    print("x = ", x )
    print("y = ", y )
    return(x+y)

two_num(55, 60)

#function to calculate average 
def avg_function(x, y):
    avg = x + y // 2
    return avg

avg_function(10, 20)

#function to calculate factorial
def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

calc_factorial(5)

#function to convert usd dollars to pkr.
def usd_converter(usd_val):
    pkr_val = usd_val * 277
    print(f"The value of USD ${usd_val} = {pkr_val} PKR")

usd_converter(2)