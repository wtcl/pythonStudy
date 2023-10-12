import string


# 检查报告函数
def output(result):
    tips = ["密码长度至少为8位；", "密码至少要包含一个大写字母；",
            "密码至少要包含一个小写字母；", "密码至少要包含一个数字；",
            "密码至少要包含一个标点符号；"]
    ret = []
    for i in range(5):
        if result[i] == 1:
            ret.append(tips[i])
    if sum(result) == 0:        # 五项条件都满足
        return "检查结果如下：密码符合规则\n密码强度：强\n"
    elif sum(result) == 1:      # 只满足4项
        return "检查结果如下：{}\n密码强度：中高\n".format("".join(list(set(ret))))
    elif sum(result) == 3 or sum(result) == 2:      # 只满足3或2项
        return "检查结果如下：{}\n密码强度：中低\n".format("".join(list(set(ret))))
    else:       # 只满足1项或0项
        return "检查结果如下：{}\n密码强度：弱\n".format("".join(list(set(ret))))


# 检查函数
def check(strings):
    # l,a,b,c,d用来代表长度，大写字母，小写字母，数字，标点符号。值为 1 表示该字符串不包含该项
    length, a, b, c, d = 1, 1, 1, 1, 1
    # 首先判断长度
    if len(strings) >= 8:
        length = 0
    strings = list(strings)
    # 针对输入的密码的每个字符进行判断
    for s in strings:
        if s in string.ascii_uppercase:
            a = 0
        elif s in string.ascii_lowercase:
            b = 0
        elif s in string.digits:
            c = 0
        elif s in string.punctuation:
            d = 0
    return [length, a, b, c, d]


def main():
    strings = input("要检查的密码: ")
    # 对输入的密码进行检查
    result = check(strings)
    # 对检查的结果生成检查报告
    output_result = output(result)
    print(output_result)


if __name__ == "__main__":
    main()
