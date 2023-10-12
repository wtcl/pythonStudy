
# 判断字符串是否相同，或者只有一个字符不同（替换）
def find_mismatch(s1, s2):
    s1 = s1.lower()  # 转为小写
    s2 = s2.lower()  # 转为小写
    if s1 == s2:  # 完全相同
        return 0
    elif len(s1) == len(s2):  # 字符串长度一致
        t = 0
        for i in range(len(s1)):  # 依次判断每个字符
            if s1[i] != s2[i]:
                t += 1
        if t == 1:  # 只有一个字符不同
            return 1
        else:  # 超过一个字符不同
            return 2
    else:  # 字符串相同
        return 2


# 判断字符串是否具有包含关系，即去除一个字符为另一个字符串
def single_insert_or_delete(s1, s2):
    s1 = s1.lower()  # 转为小写
    s2 = s2.lower()  # 转为小写
    if s1 == s2:  # 完全相同
        return 0
    elif len(s1)-len(s2) == 1:  # s1比s2长度大1
        t = 0
        for i in range(len(s1)):  # 依次去掉每个字符
            if s1[:i] + s1[i+1:] == s2:
                t += 1
        if t >= 1:  # 去除任意一个字符可以相同
            return 1
        else:
            return 2
    elif len(s2)-len(s1) == 1:  # s2比s1长度大1
        t = 0
        for i in range(len(s2)):
            if s2[:i] + s2[i+1:] == s1:
                t += 1
        if t >= 1:
            return 1
        else:
            return 2
    else:  # 其它情况
        return 2


# 语句单词修改
def spelling_corrector(s1, list2):
    list1 = s1.split()  # 将句子转为单词
    returnlist = []
    for i in range(len(list1)):
        if len(list1[i]) > 2:  # 不判断长度小于等于2的单词
            for j in range(len(list2)):  # 依次对正确的单词进行判断
                # 原单词可以替换正确单词
                if single_insert_or_delete(list1[i], list2[j]) == 1 or \
                        find_mismatch(list1[i], list2[j]) == 1:
                    returnlist.append(list2[j])
                    break  # 只替换最开始的单词
                # 原单词正确，在词库中
                elif single_insert_or_delete(list1[i], list2[j]) == 0:
                    returnlist.append(list1[i])
                    break  # 单词正确，不再判断下一个单词
            # 如果前面的筛选没有结果，则保留单词本身
            if len(returnlist) == i:
                returnlist.append(list1[i])
        else:  # 对于长度小于等于2的单词不修改
            returnlist.append(list1[i])
    return " ".join(returnlist).lower()


if __name__ == "__main__":
    print(find_mismatch("Python", "Java"))
    print(find_mismatch("Hello There", "helloothere"))
    print(find_mismatch("sin", "sink"))
    print(find_mismatch("dog", "Dog"))
    print()
    print(single_insert_or_delete("Python", "Java"))
    print(single_insert_or_delete("book", "boot"))
    print(single_insert_or_delete("sin", "sink"))
    print(single_insert_or_delete("dog", "Dog"))
    print(single_insert_or_delete("poke", "spoke"))
    print(single_insert_or_delete("poker", "poke"))
    print(single_insert_or_delete("programing", "programming"))
    print()
    print(spelling_corrector("Thes is the Firs cas", ["that", "first", "case", "car"]))
    print(spelling_corrector("programing is fan and eesy", ["programming", "this", "fun", "easy", "book"]))
    print(spelling_corrector("Thes is vary essy", ["this", "is", "very", "very", "easy"]))
    print(spelling_corrector("Wee lpve Pythen", ["we", "Live", "ln", "Python"]))