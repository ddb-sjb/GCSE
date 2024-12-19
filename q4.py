shape = input("triangle or square: ")
size = int(input("Size: "))
if shape in ["square","s"]:
    line = size*'*'
    print(line)
    for i in range(0,size-1):
        print(line)
else:
    line= '*'
    print(line)
    for i in range(0,size-1):
        line = line + '*'
        print(line)


#### D3C0R@T1ON5