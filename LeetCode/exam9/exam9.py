'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''

def isPalindrome(x):
    num = 0
    temp_x = x
    while(x/10):
        num = num*10 + x%10
        x = int(x/10)

    if num == temp_x:
        return True
    else:
        return False


def main():
    n = (int)(input("input a number:"))
    nnn = isPalindrome(n)
    print(nnn)



if __name__ == "__main__":
    main()