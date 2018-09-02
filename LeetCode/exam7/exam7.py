
'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
'''
'''
Given a 32-bit signed integer, reverse digits of an integer.
'''

def reserve(x):
    x1 = int(x)
    num = 0

    if x1>0:
        for _ in range(len(x)):
            num = num*10+x1%10
            x1 = int(x1/10)
    else:
        x1 = x1 * (-1)
        for _ in range(len(x)-1):
            num = num*10+x1%10
            x1 = int(x1/10)
        num = num * (-1)

    return num


def main():
    x = input("input a number:")
    print("%d" ,x)
    y = reserve(x)
    print(y)

if __name__ == "__main__":
    main()