word = input("Word: ")
newword = ""
for i in range(0,len(word)):
    if i%2 == 0:
        newword = newword + word[i].upper()
    else:
        newword = newword + word[i].lower()

print(newword)

### M1X3D

