from decimal import Decimal


# 采用decimal模块，使得循环的次数可达到 830483，而不报错
def decimal_math_pi(num):
    sum = 0
    for i in range(num):
        sum += (Decimal(4)/(Decimal(8)*Decimal(i)+Decimal(1)) -
                Decimal(2)/(Decimal(8)*Decimal(i)+Decimal(4)) -
                Decimal(1)/(Decimal(8)*Decimal(i)+Decimal(5)) -
                Decimal(1)/(Decimal(8)*Decimal(i)+Decimal(6)))/Decimal(16)**i
    return sum


# 采用普通的计算方式，可以使得输入的循环次数达到256
def normal_math_pi(num):
    sum = 0
    for i in range(num):
        sum += (4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))/16**i
    return sum


if __name__ == "__main__":
    num = int(input("Please input a num to simulate: "))
    result = normal_math_pi(num)
    print("The result of the simulation is:", result)
    num = int(input("Please input a num to simulate: "))
    result = decimal_math_pi(num)
    print("The result of the simulation is:", result)
