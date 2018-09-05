'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''

def longestCommonPrefix(strs):
    flag = True
    length = len(strs)
    if length == 0:
        return ''
    length0 = len(strs[0])
    if length0 == 0:
        return ''
    partain = 0
    for i in range(1,length):
        length_temp = len(strs[i])
        if length_temp == 0:
            return ''
        if length0 > length_temp:
            length0 = len(strs[i])
            partain = i

    j = 0
    while flag:
        for i in range(0, length):
            if strs[i][j] == strs[partain][j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            j = j + 1
            if j == length0:
                break

    s = strs[0][0:j]
    return s


def main():
    list = ['ca','a']
    s = longestCommonPrefix(list)
    print(s)


if __name__ == '__main__':
    main()
