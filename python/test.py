from collections import OrderedDict

a = OrderedDict()
a = {"s" : 2, "d" : 3, "w" : 4}
for i in range(10  ):
    for j in a:
        print(a[j], end=" ")
    print("lol")
a['ww'] = 22
for i in a:
    print(i)