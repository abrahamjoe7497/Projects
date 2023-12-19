#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Faith Abraham"
__email__ = "fdavidkandavalli@students.columbiabasin.edu"
__course__ = "CSIT 311"
__lab__ = "Whack"
__date__ = "Feb 10, 2023"
__version__ = "0.0.1"

#libraries used
import pandas as pd
import numpy as np
import sys
import os
    
"""
Functions Portion of the Program

"""

"""
Interface 1 :: Authentication

"""
def Authenticate(user,password):
    
    success = False
    if user in list(user_df['username']):
        #print(user)
        
        #checking the dataframe for the password hash in the row that has the use value
        if user_df.loc[user_df['username'] == user, 'password'].iloc[0] == password:
            print("Authentication is Success")
            success = True    
            return success
        
        else:
            print("Error: no such password")
        
    else:
        print("Error: no such user")
    

"""

Interface 2 :: Get User Info

"""

def GetUserInfo(user):
    
    success = False
    
    if user in list(ctrl_df['users']):
        
        info = ctrl_df.iloc[ctrl_df['users'].values == user]
        print(info)
        success = True
        return success
    
    else:
        print("Error: no such user")
        

""" 

Interface 3 :: Get Object Info 

"""

def GetObjectInfo(obj):
    
    success = False
    
    if obj in list(ctrl_df):
        column_name = obj
        
        obj_values = ctrl_df.loc[:,column_name].values
        print(ctrl_df['users'].values, obj_values)
        success = True
        return success
    
    else:
        print("Error: No such object")
         

""" 

Interface 4 :: Set Object Info 

"""
def SetObjectInfo(user, obj):
    success = False
    column_name = obj
    if obj in list(ctrl_df):
        for index,row in ctrl_df.iterrows():
           
            if row['users'] == user:
                ctrl_df.at[index,column_name] = 'enabled'
                print("Success")
                success = True
                return success
            
                break
         
        else:
            print("Error: No such user")
    else:
        print("Error: No such object")
               

"""

Interface 5 :: Remove Object Info

"""

def RemoveObjectInfo(user, obj):
   
    success = False
    column_name = obj
    
    if obj in list(ctrl_df):
        for index,row in ctrl_df.iterrows():
           
            if row['users'] == user:
                ctrl_df.at[index,column_name] = ''
                print("Success")
                
                success = True
                return success
                break
        
        else:
            print("Error: No such user")
    else:
        print("Error: No such object")
        
"""
Main Portion of Program

"""

#html file to store data

fileName = "whack_data.html"

#lists used  
names = ['horace','larry','fred']

encrypt = [np.nan,np.nan,np.nan]
ssid = [np.nan,np.nan,np.nan]
channel = [np.nan,np.nan,np.nan]
report = [np.nan,np.nan,np.nan]
config = [np.nan,np.nan,np.nan]

#display settings
pd.options.display.max_rows = None
pd.options.display.max_columns = None

"""
Users and passwords dataframe

"""
users = [['horace','test123'],['larry','test123'],['fred','test123']]
user_df = pd.DataFrame(users,columns = ['username','password'])


"""
HTML File and dataframe creation for User controls
 
"""
def create_html_file():
    d = {'users':names,'get_Encryption_Type': encrypt,'get_SSID': ssid,'get_Channel':channel,'view_Report': report,'view_Configuration': config}
    df = pd.DataFrame(data=d)
    
    df.to_html(fileName,index=False)
    return df

file_exists = False

"""
check if file exists

"""

if os.path.exists(fileName):
    file_exists = True
        
#if not create file
else:
    create_html_file()
    

"""
Dataframe Access

"""
def read_file():
    df = pd.read_html(fileName)[0]
    return(df)


ctrl_df = read_file()

"""
Wrinting Changes to the User Access Control Datafile

"""

def write_file():
    ctrl_df.update(ctrl_df)
    new_df = ctrl_df.to_html(fileName, index = False)
    #print(ctrl_df)
    
    return new_df
    


"""
System Argument Calls

"""
if sys.argv[1] == "Authenticate":
	Authenticate(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "GetUserInfo":
	GetUserInfo(sys.argv[2])
elif sys.argv[1] == "GetObjectInfo":
	GetObjectInfo(sys.argv[2])
elif sys.argv[1] == "RemoveObjectInfo":
	RemoveObjectInfo(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "SetObjectInfo":
	SetObjectInfo(sys.argv[2], sys.argv[3])
else:
        print("Error: invalid syntax")
        
        
"""
Writing changes to file

"""
write_file()















    
            

         
         
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    