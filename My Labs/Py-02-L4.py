ProtocolsDict = {'FTP': '21' , 'DNS' : '53'     
    , 'LDAP' : '389' , 'MySQL' : '3306' }   #Data structure Dictionary {} 

question = str(input("For which protocol would you like to know the port number? ")).upper() 
            #takes input from user and converts to all uppercase to find match in dictionary

if question in ProtocolsDict.keys():    # Checks if question is inside Dictionary
    answer = ProtocolsDict[question]    # creates str for answer found in Dictionary  
    
    print("The port number for protocol "   
        + question + " is " + answer + "!") # Prints my question with answer 

else:
    print("The protocol can't be found") # If user input is not found in Dictionary prints this line
