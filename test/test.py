name = input("name: ")
ID = input("ID: ")
group = input("group: ")

data = name+";"+ID+";"+group

print(data)

with open("test.txt", "a") as f:
        print(data, file = f)