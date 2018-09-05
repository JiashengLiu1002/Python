'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''

def isValid(s):
    length = len(s)
    if length%2:
        return False
    temp = ''
    for j in range(length):
        if (s[j] == '(' or s[j] == '[' or s[j] == '{'):
            temp = temp + s[j]

        elif (s[j] == ')'):
            if len(temp) == 0:
                return False
            if temp[len(temp)-1] != '(':
                return False
            else:
                temp = temp[0:len(temp)-1]
        elif (s[j] == ']'):
            if len(temp) == 0:
                return False
            if temp[len(temp)-1] != '[':
                return False
            else:
                temp = temp[0:len(temp)-1]
        elif (s[j] == '}'):
            if len(temp) == 0:
                return False
            if temp[len(temp)-1] != '{':
                return False
            else:
                temp = temp[0:len(temp)-1]
    if len(temp) != 0:
        return False
    return True


def main():
    s1 = "()"
    print(isValid(s1))
    '''
    s2 = "()[]{}"
    print(isValid(s2))
    s3 = "]("
    print(isValid(s3))
    s4 = "([)]"
    print(isValid(s4))
    s5 = "(([]){})"
    print(isValid(s5))
    '''

if __name__ == '__main__':
    main()