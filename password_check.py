#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Faith Abraham"
__email__ = "fdavidkandavalli@students.columbiabasin.edu"
__course__ = "CSIT 311"
__lab__ = "Password Check"
__date__ = "Jan 23, 2023"
__version__ = "0.0.1"


#Final program version
#The program needs the lxml parser to be able to run.
#if the IDE does not contain lxml parser. Then it needs to be downloaded from "conda install lxml".

#library to create and use dataframes. 

import pandas as pd

"""
Create function to create dataframe of users and passwords and add to xml file

"""
my_password_file = 'password_check.xml'

#create xml file function 
def create_password_xml_file():
    user_data = {'username':['harry','hermione','ron'],'password':['492b0021a472dfc9b69433f04b6e75474ea8737237d489d6b026917fd713ac6c','492b0021a472dfc9b69433f04b6e75474ea8737237d489d6b026917fd713ac6c','492b0021a472dfc9b69433f04b6e75474ea8737237d489d6b026917fd713ac6c']}
    df = pd.DataFrame(data=user_data)
    
    df.to_xml(my_password_file,index = False)

#library used for manipulating hashes

import hashlib

#function to get SHA2 hash and return the hexdigest value
def gethash(password):
    password_hash = hashlib.sha256(password.encode())
    return(password_hash.hexdigest())
    
"""
Interface 1 :: User Authentication

"""            

def Authenticate(user,password):
    
    #hash the palaintext password 
    pass_hash = gethash(mypassword)
    
    #read the xml file into a datadframe
    data = pd.read_xml(my_password_file)
    
     
    success = False
    
    # checking the data list for the user value
    if user in list(data['username']):
       
        
        #checking the dataframe for the password hash in the row that has the use value
        if data.loc[data['username'] == user, 'password'].iloc[0] == pass_hash:
            #print("Authentication is Success")
            success = True  
            
        else:
            success = False
            
            print("Error: no such password")
        
    else:
        print("Error: no such user")
    
    #return the success flag
    
    return(success)
    


"""
Interface 2 :: Change User Password

"""
#library used for regular expressions
import re

#function will check if user has a profile
#then verify if the new password string is compliant with password policy requirements
#if compliant the if stateent will procede to find the row with the user and 
#the password to be updated.
#dataframe updates the password column of the user specified
#then the updated dataframe is converted into xml file

def ChangePassword(user,old_password,new_password):
    
    #print(user,old_password,new_password)
    
    Auth = Authenticate(user, old_password)
    
    if Auth == True:
        
        regular_expression = "^(?=.*[a-z]{2,})(?=.*[A-Z]{3,})(?=.*\d{2,})[A-Za-z\d]{10,14}$"
        
        # compiling regex to create regex object
        pattern = re.compile(regular_expression)
        
        # searching regex                               
        valid = re.search(pattern, new_password)
        
        #checking if the regex function matches the pattern provided to the new 
        #password supplied
        if valid != None:
            
            #hash the new password plaintext to sha2
            new_pass_hash = gethash(new_password)
            #read in the xml file as a dataframe
            df_read = pd.read_xml(my_password_file)   
            #locate the row of the specified user and update the current password
            #to new password
            df_read.loc[df_read['username'] == user, 'password'] = new_pass_hash
            #convert the updated dataframe back into xml format       
            df_read.to_xml(my_password_file)
            print("Password is Updated")
                    
        else:
            print("Error: password policy failure")
            
    else:
        print("Error: User Authentication Failure")    
    return 1
  
    
"""
Main Program

"""
# library used for input system arguments
import sys

#script arguments
script_name = sys.argv[0]
script_arguments = sys.argv[1:]
function = script_arguments[0]
myname = script_arguments[1:][0]
mypassword = script_arguments[2:][0]

#library used to check path of file in OS.
import os

#file exist flag
file_exists = False

#check is a file exists
if os.path.exists(my_password_file):
    file_exists = True

#if not create a xml file
else:
    create_password_xml_file()
    print("New Password File Created: password_check.xml")

#interface Function Calls    
if function == "Authenticate":
    if Authenticate(myname,mypassword):
        print("Authentication is Success")
    
    else:
        print(" ")
    
#changePassword function call        
elif function == "ChangePassword":
    update_password = script_arguments[3:][0]
    ChangePassword(myname,mypassword,update_password)
    
else:
    print("Error: No such Interface")
    