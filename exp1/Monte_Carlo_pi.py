from random import uniform


def mc_pi(num):
    times = 0
    for i in range(num):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if (x**2 + y**2) <= 1:
            times += 1
    return 4*times/num


if __name__ == "__main__":
    num = int(input("Please input the number to throw arrow: "))
    result = mc_pi(num)
    print("The result of pi is:%.8f" % result)
