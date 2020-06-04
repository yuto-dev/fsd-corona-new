newList = ["a;b", "c;d"]

f = open("test.txt", "w")
counter = 0
for items in newList:
    f.writelines(newList[counter])
    f.writelines("\n")
    counter = counter + 1
f.close()
#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())