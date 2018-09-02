'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

def addTwoNumbers(l1,l2):
    num1 = 0
    num2 = 0
    for i in range(len(l1)):
        num1 = num1 * 10 + (int)(l1[len(l1)-i-1])

    for i in range(len(l2)):
        num2 = num2*10 + (int)(l2[len(l2)-i-1])
    print(num1+num2)




def main():
    l1 = []
    l2 = []
    flag = True
    print("input a number")

    x = input()
    while (x != '='):
        if x == '+':
            flag = False
            x = input()
            continue
        if flag:
            l1.append(x)
        else:
            l2.append(x)
        x =input()

    addTwoNumbers(l1,l2)
'''
    print(l1)
    l1.reverse()
    print(l1)
    num1 = 0
    num2 = 0
    for i in range(0,len(l1)):
        num1= num1*10+(int)(l1[i])

    print(num1)

    l2.reverse()
    for i in range(0,len(l2)):
        num2 = num2 * 10+ (int)(l2[i])
    print(num2)
    print("%d + %d = %d" %(num1,num2,num1+num2))

'''


if __name__ == "__main__":
    main()
