#
# def test():
#     for i in range(7):
#         yield i
#
# if __name__ == "__main__":
#     arr = test()
#     print(arr)
#     for val in arr:
#         print(val)
#
# """
# <generator object test at 0x0362EFB0>
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# """

if __name__ == "__main__":
    arr = (i for i in range(5))
    print(arr) # <generator object <genexpr> at 0x032CFFB0>
