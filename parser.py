#Jessica Noel
# September 18, 2022
#CS-555 Agile Methods for Software Development

with open("/Users/jessica/Desktop/School/CS-555/M2.B3 Project 2/tree.ged") as f:
    lines = f.readlines()

#List of all supported tags including start, note, end
valid_tags =["TRLR", "HEAD", "NOTE", "SEX", "BIRT", "DEAT", "FAMC", "FAMS","MARR", "HUSB", "WIFE", "CHIL","DIV"]

newLines = []
tempString = []

for line in lines:
    sepLine = line.split()
    print(line)
    line = line.replace('\n', "")
    
    #Checks if tag is supported, if yes Y, if not N
    if (sepLine[1] in valid_tags):
        validTag = "Y"

    #Cover the two excpetions, for when INDI and FAM are 3rd token/second index
    elif (len(sepLine) == 3):
        if (sepLine[2] == 'INDI'):
            newLines.append(tempString);
            tempString = []

    tempString += sepLine

    #Cover 2 DATE, but not 1 DATE
    if ((sepLine[0] == "2") and (sepLine[1] == "DATE")):
        validTag = "Y"
    
    #Cover 1 NAME, but not 2 NAME
    elif ((sepLine[0] == "1") and (sepLine[1] == "NAME")):
        validTag = "Y"
    
    #All other variations are not supported or valid
    else:
        validTag = "N"

    args = ""
    for x in sepLine[2:len(sepLine)]:
        args += (x + " ")

    #print("--> " + line)
    
    
   
    

    #print(newLines)
    #print("<-- " + sepLine[0] + "|" + sepLine[1] + "|" + validTag + "|" + args + "\n")
    # format text
    


    # case_list = []
    # for entry in entries_list:
    #     case = {'_id': entry[0], 'key2': entry[1], 'key3':entry[2] }
    #     case_list.append(case)
idList = []
nameDic = {}
ageDic = {}
genderDic = {}
birthDayDic = {}
aliveDic = {}
deadDic = {}
childDic = {}
spouseDic = {}


#struct
# [ 
    id
]
for line in newLines:
    _id = ""
    
    for i in range(len(line)):
        day , month , year, birthDay = ''
        print(line[i])
        if (line [i] == "INDI"):
            _id = line[i - 1]
            idList.append(_id)
        if (line [i] == "NAME"):
            nameDic[_id] = line[i + 1] + " " + line[i + 2]
        if (line[i] == "BIRT"):
            day = line[i + 3]
            month = line[i + 4]
            year  = line[i + 5]
            birthDay = f'{month}/{day}/{year}'
            birthDayDic[_id] = birthDay

print (birthDayDic)

f.close()


    
    