#Lucas Wenger

#Part 1
with open("bucketlist.txt","w+") as bl: #create file and open in write+ mode
    bl.write("1. Become a motorcycle nomad\n") #write item 1, newline
    bl.write("2. Master archery\n") #write item 2, newline
    bl.write("3. Go on a sea voyage\n") #write item 3, newline
    bl.write("4. Become a master astronomer\n") #write item 4, newline
    bl.write("5. Create a game easier to learn but involves more strategy than chess") #write item 5
    
    '''
    #check to make sure file is formatted correctly
    bl.seek(0)#set cursor at beginning
    blstring = bl.read()#save as string
    print(blstring)#print string 
    '''

#Part 2
with open("bucketlist.txt","a+") as bl: #open file in append+ mode
    bl.write("\n6. Become a master at Python") #add newline and write item #6
    
    '''
    #check to make sure file is formatted correctly
    bl.seek(0)#set cursor at beginning
    blstring = bl.read()#save as string
    print(blstring)#print string 
    '''

#Part 3
with open("bucketlist.txt","r+") as bl: #open file in read+ mode
    blstring = bl.read() #save as string
    blstring = blstring.replace("Python","a new language") #replace string

with open("bucketlist.txt","w+") as bl: #open file in write+ mode
    bl.write(blstring) #open in write mode to overrwrite previous list with replaced one

    
    #check to make sure file is formatted correctly
    bl.seek(0)#set cursor at beginning
    blstring = bl.read()#save as string
    print(blstring)#print string 
    
