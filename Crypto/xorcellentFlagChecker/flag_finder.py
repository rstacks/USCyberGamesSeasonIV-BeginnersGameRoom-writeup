lst1 = [-83,117,-1,-125,-43,-64,115,22,44,42,-9,46,123,69,-76,-106,-5,-127,-87,123,105,105]
lst2 = [-2,60,-87,-63,-110,-110,8,110,28,88,-88,108,59,54,-123,-11,-120,-34,-5,72,31,20]

XORed_lst = [lst1[i] ^ lst2[i] for i in range(len(lst1))]
flag = "".join([chr(elem) for elem in XORed_lst])

print(flag)