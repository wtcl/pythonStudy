factorial_sum,factorial = 0,1
for i in range(1,11):
    factorial *= i
    factorial_sum += factorial
print("The sum of the factorial of 1 to 10: {}".format(factorial_sum))
