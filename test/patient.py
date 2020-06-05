my_file = open("patient.txt", "r") # Opens patient database and store in variable content as list
content = my_file.readlines()
my_file.close()

patientID = input("Enter patient ID: ") # Prompts user to enter patient ID

counter = 0 # Set Counter

for element in content:
    newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
    print (newContent)
    del newContent[-1]
        #print(newContent)

    if newContent[1] == patientID:

        if newContent[3] == "N":
            newContent[3] = "t1"

        elif newContent[3] == "t1":
            newContent[3] = "t2"
            print("masuk pak eko")

        elif newContent[3] == "t2":
            newContent[3] = "t3"

        elif newContent[3] == "t3":
            newContent[3] = "F"

        else:
            print("mampus")       

    newPatientData = newContent[0]+";"+newContent[1]+";"+newContent[2]+";"+newContent[3]+";"+"X\n"
    print(newPatientData)

    patientID = int(patientID)

    newIndex = patientID - 1

    content[newIndex] = newPatientData

    #print(content)  

print(content)

f = open("patient.txt", "w")
counter = 0
for items in content:
    f.writelines(content[counter])
    #f.writelines("\n")
    counter = counter + 1
f.close()
#open and read the file after the appending:
f = open("patient.txt", "r")
print(f.read())