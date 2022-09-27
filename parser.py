#Jessica Noel, Brendan Probst, John Schneiderhan
# September 18, 2022
#CS-555 Agile Methods for Software Development
from datetime import *
from prettytable import PrettyTable
with open("gedcomTest.txt") as f:
    lines = f.readlines()

#List of all supported tags including start, note, end
valid_tags =["TRLR", "HEAD", "NOTE", "SEX", "BIRT", "DEAT", "FAMC", "FAMS","MARR", "HUSB", "WIFE", "CHIL","DIV"]

newLines = []
tempString = []

for line in lines:
    sepLine = line.split()
    line = line.replace('\n', "")
    
    #Checks if tag is supported, if yes Y, if not N
    if (sepLine[1] in valid_tags):
        validTag = "Y"

    #Cover the two excpetions, for when INDI and FAM are 3rd token/second index
    elif (len(sepLine) == 3):
        if (sepLine[2] == 'INDI' or sepLine[2] == 'FAM'):
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


##INDIVIDUAL STUFF
idList = []
famIdList = []
nameDic = {}
ageDic = {}
genderDic = {}
birthDayDic = {}
aliveDic = {}
deadDic = {}

#MARRIAGE STUFF
childDic = {}
wifeDic = {}
husbandDic = {}
spouseDic = {}
marriedDic = {}
divorcedDic = {}


for line in newLines:
    _id = ""
    _famId = ""
    birthYear = 0
    deathYear = 0
    isAlive = True
    for i in range(len(line)): 
        # print(line[i])
        if (line [i] == "INDI"):
            _id = line[i - 1]
            idList.append(_id)
        if (line[i] == "FAM"):
            _famId = line[i - 1]
            famIdList.append(_famId)
        if (line [i] == "NAME"):
            nameDic[_id] = line[i + 1] + " " + line[i + 2]
        if (line[i] == "BIRT"):
            day = ""
            month = ""
            year = "" 
            birthDay = ""
            day = line[i + 3]
            month = line[i + 4]
            year  = line[i + 5]
            birthDay = f'{month}/{day}/{year}'
            birthDayDic[_id] = birthDay
            year = int(year)
            birthYear = year
            age = 2022 - year
            ageDic[_id] = age
        if (line[i] =="DEAT"):
            day = ""
            month = ""
            year = "" 
            deathDay = ""
            if (line[i + 1] == "N"):
                #they're allive
                isAlive = True
                deadDic[_id] = "NA"
                aliveDic[_id] = isAlive4
            elif (line[i + 1] == "Y"):
                isAlive = False
                aliveDic[_id] = isAlive
                #they dead
            aliveDic[_id] = isAlive
            if not(isAlive):
                day = line[i + 4]
                month = line[i + 5]
                year  = line[i + 6]
                deathYear = int(year)
                age = deathYear - birthYear
                ageDic[_id] = age
                deathDay = f'{month}/{day}/{year}'
                deadDic[_id] = deathDay
        if (isAlive):
            isAlive = True
            deadDic[_id] = "NA"
            aliveDic[_id] = isAlive
        if (line[i] == "SEX"):
            genderDic[_id] = line[i + 1]
        if (line[i] == "CHIL"):
            childDic[line[i + 1]] = _famId
        if (line[i] == "WIFE" or line[i] == "HUSB"):
            spouseDic[line[i + 1]] = _famId
            if (line[i] == "WIFE"):
                wifeDic[_famId] = line[i + 1]
            else:
                husbandDic[_famId] = line[i + 1]
        if (line[i] == "MARR"):
            day = line[i + 2]
            month = line[i + 3]
            year = line[i + 4]
            date = f"{month}/{day}/{year}"
            marriedDic[_famId] = date
        if (line[i] == "DIV"):
            day = line[i + 2]
            month = line[i + 3]
            year = line[i + 4]
            date = f"{month}/{day}/{year}"
            divorcedDic[_famId] = date
        
    #now the person is complete

x = PrettyTable()
x.field_names = ["ID", "NAME", "GENDER","BIRTHDAY", "AGE", "ALIVE", "DEATH", "CHILD", "SPOUSE"]
for id in idList:
    if(not childDic.get(id)):
        childDic[id] = "NA"
    if(not spouseDic.get(id)):
        spouseDic[id] = "NA"
    newRow = [id,nameDic.get(id),genderDic.get(id),birthDayDic.get(id),ageDic.get(id),aliveDic.get(id), deadDic.get(id), childDic.get(id), spouseDic.get(id)]
    x.add_row(newRow)
print(x)
y = PrettyTable()
y.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND NAME", "HUSBAND ID", "WIFE NAME", "WIFE ID", "CHILDREN"]
for famId in famIdList:
    if(not marriedDic.get(famId)):
        marriedDic[famId] = "NA"
    if(not divorcedDic.get(famId)):
        divorcedDic[famId] = "NA"
    children = []
    for childId in childDic:
        if childDic[childId] == famId:
            children.append(childId)
    newRow = [famId, marriedDic.get(famId), divorcedDic.get(famId), nameDic.get(husbandDic.get(famId)), husbandDic.get(famId), nameDic.get(wifeDic.get(famId)), wifeDic.get(famId), children]
    y.add_row(newRow)
print(y)
f.close()