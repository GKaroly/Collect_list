#!/usr/bin/python

import sys
import os.path
import json
import datetime
import time
#import strftime

# This program reads a text file as input which contains elements line by line
# Each of the line is a value. This values are following eachother and must be process
# The program construct a json object and write out into an output file

def main():

    #Check parameters
    if len(sys.argv)!=3:
        print("The program accept only 2 input.")
        sys.exit()
    
    input_file_name=sys.argv[1] 
    output_file_name=sys.argv[2]
    print('Input file name: ', input_file_name)
    print("Output file name: ", output_file_name)

    #Check if inputfile exist
    if os.path.isfile(input_file_name):
        print("Input file exist")
    else:
        print("Input file not exist.")
        sys.exit()

    #Get actual datetime to items property and filename
    datetime_in_date=datetime.datetime.now()
    datetime_in_string=datetime_in_date.strftime("%Y-%m-%d %H_%M_%S")

    #Read the inputfile
    lines=[]
    with open(input_file_name, 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()

    ctr=1
    temp_user_name=""
    temp_user_real_name=""
    temp_json={}

    jsonData={}
    jsonData["elements"]=[]

    #Go through the elements and create json object
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
            temp_json["registered_date"]=datetime_in_string
            temp_json["state"]="actual follow"
            temp_json["sign"]="0"
            jsonData["elements"].append(temp_json)

        ctr=ctr+1

    output_file_name=output_file_name+" "+datetime_in_string
    
    #Create the outputFile
    if os.path.isfile(output_file_name):
        print("Output file exist")
        sys.exit()
    else:
        output_file_name=output_file_name+".txt"

        #From here: https://stackoverflow.com/questions/43255909/sort-a-json-using-python
        jsonData['elements'] = sorted(jsonData['elements'], key=lambda k: k['user_name'])
        writeIntoFiles(output_file_name, jsonData)


def writeIntoFiles(output, jsonData):
    with open(output, 'w') as outfile:
        json.dump(jsonData, outfile, indent=4, sort_keys=True)
        


if __name__ == "__main__":
    main()
