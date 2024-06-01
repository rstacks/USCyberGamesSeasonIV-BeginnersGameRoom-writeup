flagCheck = [45, 55, 42, 62, 57, 46, 5, 10, 77, 14, 7, 33, 28, 79, 26, 26, 79, 29, 11, 20, 12, 33, 16, 31, 13, 13, 9, 80, 14, 28, 3]
flagList = [chr(128 - flagCheck[i]) for i in range(len(flagCheck))]
print("".join(flagList))
