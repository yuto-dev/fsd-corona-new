def bacafile():
    my_file = open("patient.txt", "r")
    content = my_file.readlines()
    #print(content)
    d5 ='t3'    
    d8 = '0'
    userid ='3'
    data=''
    xdat=''
    
    for ele in content:
        xcon = ele.split(';')
        del xcon[-1] 

        for i in range(len(xcon)):
                        
            if xcon[1] == '3':
                if i==5:
                    xdat = xdat + d5+';'
                elif i==8:
                    xdat = xdat + d8+';'    
                else:    
                    xdat = xdat + xcon[i]+';'                
            
    print(xdat)    
    #newcon.append(databaru)
    #--- Tulis ke file

bacafile()