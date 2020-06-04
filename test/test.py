newList = ["a", "b"]

f = open("test.txt", "w")
for items in newList:
    f.writelines(newList)
    f.writelines("\n")
f.close()
#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())