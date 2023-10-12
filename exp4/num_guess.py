from random import randint


# 猜数函数
def guess(result, times):
    for i in range(times):
        # 正确输入判断部分，要求输入整数
        while 1:
            num = input("Please input your guess(1--10):")
            if num.isdigit():
                break
            else:
                print("Input error!!! Please input a integer!")
        if int(num) == result:
            return 1
        elif int(num) > result:
            print("Guess error! It is too big!")
        elif int(num) < result:
            print("Guess error! It is too small!")
    return 0


# 主函数
def main():
    times = 5  # 定义最大猜测次数
    ctimes = [0, 0]  # 记录成功的次数和总次数
    while 1:
        # 每轮随机生成一个随机数
        result = randint(1, 10)
        # 进入猜数函数
        res = guess(result, times)
        # 记录次数
        ctimes[-1] += 1
        # 如果猜对了
        if res:
            # 记录对的次数
            ctimes[0] += 1
            newgame = input("You win the game! "
                            "Do you want to start a new game?[Yes/No]")
            if newgame == "Yes" or newgame == "Y":
                pass
            else:
                print("You have {} times games, and win {} times.".format(
                    str(ctimes[-1]), str(ctimes[0])))
                break
        # 如果未猜对
        else:
            print("You have used all chances! Challenging failed!")
            print("The result is {}.".format(str(result)))
            print("You have {} times games, and win {} times.".format(
                str(ctimes[-1]), str(ctimes[0])))
            break


if __name__ == "__main__":
    main()
