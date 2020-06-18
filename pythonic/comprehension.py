
# if __name__ == "__main__":
#     arr = []
#     for i in range(0, 10):
#         arr.append(i)
#     print(arr)

# if __name__ == "__main__":
#     arr = [i for i in range(0, 10)]
#     print(arr)

# if __name__ == "__main__":
#     arr = [0 for _ in range(0, 10)]
#     print(arr) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#     arr = [i*i for i in range(0, 10)]
#     print(arr) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
#     data = [100, 200, 300, 400]
#     arr = [val / 100 for val in data]
#     print(arr) # [1.0, 2.0, 3.0, 4.0]

# if statement
# if __name__ == "__main__":
#     arr = [i for i in range(0, 10) if i % 2 == 0]
#     print(arr) # [0, 2, 4, 6, 8]
#
#     arr = [i if i % 2 == 0 else 0 for i in range(0, 10)]
#     print(arr) # [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]


#two demension
if __name__ == "__main__":
    arr = [[0 for _ in range(5)] for _ in range(5)]
    print(arr)