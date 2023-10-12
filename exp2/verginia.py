from itertools import cycle


# 加密函数
def encrypt(key, message):
    key = cycle(key)
    message = list(message)
    cipher = []
    # 遍历每个字符进行加解密
    for i in range(len(message)):
        # 判断是否为字母
        if message[i].isalpha():
            # 获取下一个加密密钥字母
            k = key.__next__()
            kindex = (ord(k) - ord("A"))
            # 判断是否为大写，大写小写加密所作处理不同
            if message[i] <= "Z":
                cipher.append(chr(ord("A") +
                                  (ord(message[i]) - ord("A") + kindex) % 26))
            else:
                cipher.append(chr(ord("a") +
                                  (ord(message[i]) - ord("a") + kindex) % 26))
        else:
            cipher.append(message[i])
    return "".join(cipher)


# 解密函数
def decrypt(key, cipher):
    key = cycle(key)
    cipher = list(cipher)
    message = []
    # 遍历每个字符进行加解密
    for i in range(len(cipher)):
        # 判断是否为字母
        if cipher[i].isalpha():
            # 获取下一个加密密钥字母
            k = key.__next__()
            kindex = (ord(k) - ord("A"))
            # 判断是否为大写，大写小写加密所作处理不同
            if cipher[i] <= "Z":
                message.append(chr(ord("A") +
                                   (ord(cipher[i]) - ord("A") - kindex) % 26))
            else:
                message.append(chr(ord("a") +
                                   (ord(cipher[i]) - ord("a") - kindex) % 26))
        else:
            message.append(cipher[i])
    return "".join(message)


def main():
    # 输入明文数据
    message = input("Please input the message: ")
    # 此部分主要是为了让用户输入的密钥不会出错
    while 1:
        key = input("Please input the key: ")
        if key.isalpha():
            break
        else:
            print("Input error! Please input again!")
    # 提前将输入的小写字母转化为大写
    key = key.upper()
    # 数据加密
    cipher = encrypt(key, message)
    print("cipher:", cipher)
    # 数据解密
    message = decrypt(key, cipher)
    print("message:", message)


if __name__ == "__main__":
    main()
