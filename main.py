#!/usr/bin/python

import sys
import os.path

import json

# This program reads a text file as input which contains elements line by line
# Each of the line is a value. This values are following eachother and must be process
# The program construct a json object and write out into an output file

def main():

    if len(sys.argv)!=2:
        print("The program accept only 1 input.")
        sys.exit()
    
    

    param_1=sys.argv[1] 
    print('Input file name: ', param_1)

    if os.path.isfile(param_1):
        print("File exist")
    else:
        print("File not exist.")
        sys.exit()

    lines=[]
    with open(param_1, 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()


    ctr=1
    temp_user_name=""
    temp_user_real_name=""
    temp_json={}

    jsonData={}
    jsonData["elements"]=[]

    for item in lines:
        if(item[-1]=="\n"):
            item=item[0:-1]

        if ctr%2==1:
            temp_user_name=(item)

        if ctr%2==0:
            temp_user_real_name=(item)

            temp_json={}
            temp_json["user_name"]=temp_user_name
            temp_json["user_real_name"]=temp_user_real_name

            jsonData["elements"].append(temp_json)

        ctr=ctr+1
    


    writeIntoFiles("output.txt", jsonData)


def writeIntoFiles(output, jsonData):
    with open(output, 'w') as outfile:
        json.dump(jsonData, outfile, indent=4, sort_keys=True)
        

def removeEnterCharacterFromString(inputString):
    if inputString[-1:-2]=="\n":
        print("ITT")
    else:
        print("OTT")

if __name__ == "__main__":
    main()
