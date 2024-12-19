list1 = input("List 1 Names: ")
list2 = input("List 2 Names: ")

list1 = list1.split(",")
list2 = list2.split(",")



for i in list1:
    for j in list2:
        print(i+' - '+j)

#### N@M35