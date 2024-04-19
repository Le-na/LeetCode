# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         s = input()
#         asc = 0
#         for i in s:
#             asc += ord(i)
#         print(asc)
#
# if __name__ == '__main__':
#     Solution()

# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         self.s = s
#         self.s = [ord(x) for x in input()]
#         k = 2
#         for i in range(len(self.s) - k + 1):
#             print(i)
#         print(sum(self.s))
# #
# #
# if __name__ == '__main__':
#     Solution()


# def scoreOfString():
#     s = {ord(x) for x in input()}
#     s = list(s)
#     for i in range(len(s)):
#         result = (s[i] - s[i+1]) + (s[i+1] - s[i])
#         print(s[i], s[i+1])
#         print(result)
#     # print(type(sum(s)))
# #
# scoreOfString()


# 1
def scoreOfString():
    s = [ord(x) for x in input()]
    result = 0
    for i in range(1, len(s)):
        result += abs(s[i] - s[i-1])
    print(result)
    # print(type(sum(s)))

scoreOfString()

# 2
# def scoreOfString():
#     s = [ord(x) for x in input()]
#     print('s', s)
#     result = 0
#     previous_num = None
#
#     for num in s:
#         if previous_num:
#             result += abs(num - previous_num)
#         previous_num = num
#     print(result)
#
# scoreOfString()