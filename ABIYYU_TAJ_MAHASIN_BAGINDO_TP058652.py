#ABIYYU TAJ MAHASIN BAGINDO
#TP058652

def menu():

    print("Welcome")
    print("1. Register new patient")
    print("2. Test patients")
    print("3. Modify patient status")
    print("4. Statistics")
    print("5. Search")
    print("6. Exit")

    option = input("Choose option : ")

    if option == "1":
        registerPatient()
    elif option == "2":
        testPatient()
    elif option == "3":
        modifyPatient()
    elif option == "4":
        getStatPatient()
    elif option == "5":
        searchPatient()
    elif option == "6":
        print("Goodbye")
    else:
        print("Invalid option, please try again")        
        menu()        

#TODO: Change the return to menu option into a function

def registerPatient():
    # This module registers patients
    patientName = input("Enter patient name: ")
    patientID = input("Enter patient ID: ")
    patientMail = input("Enter patient email: ")
    print("== Groups List ==")
    print("ATO: Asymptomatic Travelled Overseas")
    print("ACC: Asymptomatic Close Contact")
    print("AEO: Asymptomatic Event Outbreak")
    print("SID: Symptomatic Individual")
    print("AHS: Asymptomatic Hospital Staff")
    patientGroup = input("Enter patient group: ")
    patientCondition = input("Any past medical conditions? (A for yes, B for no): ")
    patientZone = input("Enter patient zone (A, B, C, or D): ") #TODO: change lowercase groups to uppercase

    patientData = patientName+";"+patientID+";"+patientMail+";"+patientGroup+";"+patientZone+";"+"N"+";"+"N"+";"+"N"+";"+"N"+";"+"0"+";"+"N"+";"+patientCondition+";"+"X"
    print(patientData)

    with open("patient.txt", "a") as f:
        print(patientData, file = f)

    exitMenu()    
    
def testPatient():
    # This module handles all testing
    my_file = open("patient.txt", "r") # Opens patient database and store in variable content as list
    content = my_file.readlines()

    patientID = input("Enter patient ID: ") # Prompts user to enter patient ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[1] == patientID: # Patient found, things actually start to work here
            print("Testing patient " + newContent[0])

            print(newContent)

            print("Enter test result: ")
            print("1. Positive")
            print("2. Negative")
            testResult = input("Choose option: ")
            
            patientTest, testSolution, testResult, positive = testLaboratory(newContent[3],newContent[5],testResult)                  

            if testSolution == "QHNF" and newContent[11] == "1":
                newSolution = "quarantine in ICU, (No follow-up test required)"
            elif testSolution == "QHNF" and newContent[11] == "2":
                newSolution = "quarantine in hospital normal ward, (No follow up test required)"
            elif testSolution == "HQNF":
                newSolution = "home quarantine, (No follow-up test required)"
            elif testSolution == "QDFR":
                newSolution = "quarantine in designated centres, (Follow-up test required)"
            elif testSolution == "HQFR":
                newSolution = "home quarantine, (Follow-up test required)" 
            elif testSolution == "RU":
                newSolution = "go home and reunite with family, (No follow-up test required)"
            elif testSolution == "CW":
                newSolution = "work, (No follow-up test required)"           
           

            print("Patient should do " + newSolution)

            if patientTest == "N":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[6] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t1"
                    newContent[6] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()
            elif patientTest == "t1":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[7] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t2"
                    newContent[7] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()
            elif patientTest == "t2":
                if testResult == "1":
                    newContent[5] = "F"
                    newContent[8] = "1"
                    newContent[9] = input("Enter case ID: ")
                    newContent[10] = "A"
                elif testResult == "0":
                    newContent[5] = "t3"
                    newContent[8] = "0"
                else:
                    print("Incorrect test result, returning to main menu")
                    menu()

            newPatientData = patientBuilder(newContent)
            
            newIndex = int(newContent[1]) - 1
            content[newIndex] = newPatientData

            f = open("patient.txt", "w")
            counterIn = 0
            for items in content:
                f.writelines(content[counterIn])
                counterIn = counterIn + 1
            f.close()
                #open and read the file after the appending:
            f = open("patient.txt", "r")          


            #newPatientData = newContent[0]+";"+       

            break
            

        counter = counter + 1
        
    my_file.close()

    exitMenu()
    
def modifyPatient():
    print("Available options")
    print("1. Set all non-active positive patients' status to positive")
    print("2. Modify patient status")
    print("3. Return to main menu")
    option = input("Choose option: ")

    if option == "1":
        modifyFeatureA()
    elif option == "2":
        modifyFeatureB()
    elif option == "3":
        menu()
    else:
        print("Wrong option, please choose from the")
        modifyPatient()        

def getStatPatient():
    #This module displays the requested statistics
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    print(content)

    counter = 0

    totalTest = 0

    patientTested = 0

    patientRecovered = 0

    patientPositiveGroupATO = 0
    patientPositiveGroupACC = 0
    patientPositiveGroupAEO = 0
    patientPositiveGroupSID = 0
    patientPositiveGroupAHS = 0

    ActiveCaseZoneA = 0
    ActiveCaseZoneB = 0
    ActiveCaseZoneC = 0
    ActiveCaseZoneD = 0

    for element in content:
        newContent = content[counter].split(";")
        del newContent[-1]
        print(newContent)

        if newContent[5] != "N":
            patientTested = patientTested + 1

        if newContent[6] != "N":
            totalTest = totalTest + 1
        if newContent[7] != "N":
            totalTest = totalTest + 1
        if newContent[8] != "N":
            totalTest = totalTest + 1    

        if newContent[10] == "R":
            patientRecovered = patientRecovered + 1       

        if newContent[3] == "ATO" and newContent[6] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[7] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1
        if newContent[3] == "ATO" and newContent[8] == "1":
            patientPositiveGroupATO = patientPositiveGroupATO + 1

        if newContent[3] == "ACC" and newContent[6] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[7] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1
        if newContent[3] == "ACC" and newContent[8] == "1":
            patientPositiveGroupACC = patientPositiveGroupACC + 1

        if newContent[3] == "AEO" and newContent[6] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[7] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1
        if newContent[3] == "AEO" and newContent[8] == "1":
            patientPositiveGroupAEO = patientPositiveGroupAEO + 1

        if newContent[3] == "SID" and newContent[6] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[7] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1
        if newContent[3] == "SID" and newContent[8] == "1":
            patientPositiveGroupSID = patientPositiveGroupSID + 1

        if newContent[3] == "AHS" and newContent[6] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[7] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1
        if newContent[3] == "AHS" and newContent[8] == "1":
            patientPositiveGroupAHS = patientPositiveGroupAHS + 1   

        if newContent[4] == "A" and newContent[10] == "A":
            ActiveCaseZoneA = ActiveCaseZoneA + 1     

        if newContent[4] == "B" and newContent[10] == "A":
            ActiveCaseZoneB = ActiveCaseZoneB + 1 

        if newContent[4] == "C" and newContent[10] == "A":
            ActiveCaseZoneC = ActiveCaseZoneC + 1 

        if newContent[4] == "D" and newContent[10] == "A":
            ActiveCaseZoneD = ActiveCaseZoneD + 1                      
                    
        
        counter = counter+1

    totalTest = str(totalTest)

    patientTested = str(patientTested)

    patientRecovered = str(patientRecovered)

    patientPositiveGroupATO = str(patientPositiveGroupATO)
    patientPositiveGroupACC = str(patientPositiveGroupACC)
    patientPositiveGroupAEO = str(patientPositiveGroupAEO)
    patientPositiveGroupSID = str(patientPositiveGroupSID)
    patientPositiveGroupAHS = str(patientPositiveGroupAHS)

    ActiveCaseZoneA = str(ActiveCaseZoneA)
    ActiveCaseZoneB = str(ActiveCaseZoneB)
    ActiveCaseZoneC = str(ActiveCaseZoneC)
    ActiveCaseZoneD = str(ActiveCaseZoneD)

    print("")
    print("Total tests: " + totalTest)
    print("")
    print("Tested patients: " + patientTested)
    print("")
    print("Patient recovered: " + patientRecovered)
    print("")
    print("Asymptomatic Travelled Overseas tested positive: " + patientPositiveGroupATO)
    print("Asymptomatic Close Contact tested positive: " + patientPositiveGroupACC)
    print("Asymptomatic Event Outbreak tested positive: " + patientPositiveGroupAEO)
    print("Symptomatic Individuals tested positive: " + patientPositiveGroupSID)
    print("Asymptomatic Hostpital Staffs tested positive: " + patientPositiveGroupAHS)
    print("")
    print("Active cases in Zone A: " + ActiveCaseZoneA)
    print("Active cases in Zone B: " + ActiveCaseZoneB)
    print("Active cases in Zone C: " + ActiveCaseZoneC)
    print("Active cases in Zone D: " + ActiveCaseZoneD)
    print("")

    my_file.close()

    exitMenu()

def searchPatient():
    print("Available options")
    print("1. Patient records")
    print("2. Case status")
    print("3. Deceased patient records")
    print("4. Return to main menu")
    option = input("Choose option: ")

    if option == "1":
        searchFeatureA()
    elif option == "2":
        searchFeatureB()
    elif option == "3":
        searchFeatureC()
    elif option == "4":
        menu()    
    else:
        print("Wrong option, please choose from the")
        modifyPatient()    

def exitMenu():
    print("Return to menu?")
    print("1. Return to menu")
    print("2. Exit")
    exitOption = input("Choose option: ")

    if exitOption == "1":
        menu()
    elif exitOption == "2":
        print("Goodbye and have a nice day.")
    else:
        print("You entered the wrong option but goodbye and have a nice day. ;)")

def patientBuilder(patient):
    patientData = patient[0] +";"+ patient[1] +";"+ patient[2] +";"+ patient[3] +";"+ patient[4]+";"+patient[5]+";"+patient[6]+";"+patient[7]+";"+patient[8]+";"+patient[9]+";"+patient[10]+";"+patient[11]+";"+"X\n"
    return patientData

def testLaboratory(patientGroup, patientTest, testResult):

    if testResult == "2":
        testResult = "0"

    if patientTest == "N": # First test
                
        if testResult == "1": # First test positive 
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")

            positive = 1    
                

        elif testResult == "0": # First test negative

            if patientGroup == "ATO":
                testSolution = "QDFR"
            elif patientGroup == "ACC":
                testSolution = "QDFR"  
            elif patientGroup == "AEO":
                testSolution = "QDFR"
            elif patientGroup == "SID":
                testSolution = "HQFR"    
            elif patientGroup == "AHS":
                testSolution = "CWFR"
            else:
                print("Invalid Group")

            positive = 0    

    elif patientTest == "t1": # Second test

        if testResult == "1": # Second test positive
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")

            positive = 1     

        elif testResult == "0": # Second test negative

            if patientGroup == "ATO":
                testSolution = "QDFR"
            elif patientGroup == "ACC":
                testSolution = "QDFR"  
            elif patientGroup == "AEO":
                testSolution = "QDFR"
            elif patientGroup == "SID":
                testSolution = "HQFR"    
            elif patientGroup == "AHS":
                testSolution = "CWFR"
            else:
                print("Invalid Group")

            positive = 0    

    elif patientTest == "t2": # Third test
        
        if testResult == "1": # Third test positive
                    
            if patientGroup == "ATO":
                testSolution = "QHNF"
            elif patientGroup == "ACC":
                testSolution = "QHNF"  
            elif patientGroup == "AEO":
                testSolution = "QHNF"
            elif patientGroup == "SID":
                testSolution = "QHNF"    
            elif patientGroup == "AHS":
                testSolution = "HQNF"
            else:
                print("Invalid Group")

            positive = 1     

        elif testResult == "0": # Third test negative

            if patientGroup == "ATO":
                testSolution = "RU"
            elif patientGroup == "ACC":
                testSolution = "RU"  
            elif patientGroup == "AEO":
                testSolution = "RU"
            elif patientGroup == "SID":
                testSolution = "RU"    
            elif patientGroup == "AHS":
                testSolution = "CW"
            else:
                print("Invalid Group")

            positive = 0

    else:
        print("No tests required for this patient, returning to main menu")
        testSolution = 0
        positive = 0
        menu()            

    return patientTest, testSolution, testResult, positive               
    
def modifyFeatureA():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]

        
        print(newContent)
        if newContent[6] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[7] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"
        if newContent[8] == "1":
            if newContent[10] == "N":
                newContent[10] = "A"

        newPatientData = patientBuilder(newContent)

        print(newPatientData)

        newIndex = int(newContent[1]) - 1
        content[newIndex] = newPatientData

        f = open("patient.txt", "w")
        counterIn = 0
        for items in content:
            f.writelines(content[counterIn])
            counterIn = counterIn + 1
        f.close()
            #open and read the file after the appending:
        f = open("patient.txt", "r")


        counter = counter + 1

    print("All active patients' status has been changed to Active!")

    exitMenu()    

def modifyFeatureB():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    patientID = input("Enter patient ID: ") # Prompts user to enter patient ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[1] == patientID: # Patient found, things actually start to work here
            print("Modify patient " + newContent[0] + "'s status to?")
            print("1. Recovered")
            print("2. Deceased")
            print("3. Go back to the main menu")
            option = input("Choose option: ")

            if option == "1":
                newContent[10] = "R"
            elif option == "2":
                newContent[10] = "D"
            elif option == "3":
                menu()

            newPatientData = patientBuilder(newContent)

            newIndex = int(newContent[1]) - 1

            content[newIndex] = newPatientData

            f = open("patient.txt", "w")
            counterIn = 0
            for items in content:
                f.writelines(content[counterIn])
                counterIn = counterIn + 1
            f.close()
                #open and read the file after the appending:
            f = open("patient.txt", "r")

            break

    counter = counter + 1    

def searchFeatureA():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    print("Available options")
    print("1.Search by name")
    print("2.Search by ID")
    option = input("Choose option: ")

    if option == "1":
        patientName = input("Enter patient name (case sensitive): ")

        counter = 0

        for element in content:

            newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
            del newContent[-1]
            #print(newContent)

            if newContent[0] == patientName: # Patient found, things actually start to work here

                if newContent[10] == "N":
                    status = "Healthy"
                elif newContent[10] == "A":
                    status = "Infected"
                elif newContent[10] == "R":
                    status = "Recovered"
                elif newContent[10] == "D":
                    status = "Deceased"
                else:
                    status = "status not found"

                if newContent[11] == "1":
                    cond = "Yes"
                elif newContent[11] == "2":
                    cond = "No"
                else:
                    print("condition not found")        

                print("Patient name: " + newContent[0])
                print("Patient ID: " + newContent[1])
                print("Patient mail: " + newContent[2])
                print("Patient group: " + newContent[3])
                print("Patient zone: " + newContent[4])
                print("Patient status: " + status)
                print("Have any past medical condition: " + cond)

                exitMenu()

        counter = counter + 1

    elif option == "2":

        patientID = input("Enter patient ID: ")

        counter = 0

        for element in content:

            newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
            del newContent[-1]
            #print(newContent)

            if newContent[1] == patientID: # Patient found, things actually start to work here

                if newContent[10] == "N":
                    status = "Healthy"
                elif newContent[10] == "A":
                    status = "Infected"
                elif newContent[10] == "R":
                    status = "Recovered"
                elif newContent[10] == "D":
                    status = "Deceased"
                else:
                    status = "status not found"

                if newContent[11] == "1":
                    cond = "Yes"
                elif newContent[11] == "2":
                    cond = "No"
                else:
                    print("condition not found")        

                print("Patient name: " + newContent[0])
                print("Patient ID: " + newContent[1])
                print("Patient mail: " + newContent[2])
                print("Patient group: " + newContent[3])
                print("Patient zone: " + newContent[4])
                print("Patient status: " + status)
                print("Have any past medical condition: " + cond)

                exitMenu()

        counter = counter + 1

def searchFeatureB():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    caseID = input("Enter case ID: ") # Prompts user to enter patient ID

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]
        #print(newContent)

        if newContent[9] == caseID: # Patient found, things actually start to work here
            
            if newContent[10] == "A":
                status = "Active"
            elif newContent[10] == "R":
                status = "Recovered"
            elif newContent[10] == "D":
                status = "Deceased"
            else:
                status = "status not found"            
            
            print("Patient status for case " + newContent[9] + " is " + status)

            exitMenu()

        counter = counter + 1            

def searchFeatureC():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()

    counter = 0 # Set Counter

    for element in content:
        newContent = content[counter].split(";") # Splits the list "content" into multiple individuals as newContent
        del newContent[-1]

        if newContent[10] == "R":

            if newContent[11] == "1":
                cond = "Yes"
            elif newContent[11] == "2":
                cond = "No"
            else:
                print("condition not found")        

            print("---------------------------------")
            print("Patient name: " + newContent[0])
            print("Patient ID: " + newContent[1])
            print("Patient mail: " + newContent[2])
            print("Patient group: " + newContent[3])
            print("Patient zone: " + newContent[4])
            print("Patient case ID: " + newContent[9])
            print("Have any past medical condition: " + cond)
            print("---------------------------------")

        counter = counter + 1            
    exitMenu()

# Run program    
menu()