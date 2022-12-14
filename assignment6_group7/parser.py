#Jessica Noel, Brendan Probst, John Schneiderhan
# September 18, 2022
#CS-555 Agile Methods for Software Development
from datetime import *
from prettytable import PrettyTable
from validate import *
with open("Sprint2/SprintTwoErrorCheck.ged") as f:
    lines = f.readlines()

#List of all supported tags including start, note, end
valid_tags =["TRLR",
             "HEAD",
             "NOTE",
             "SEX",
             "BIRT",
             "DEAT",
             "FAMC",
             "FAMS",
             "MARR",
             "HUSB",
             "WIFE",
             "CHIL",
             "DIV"]

newLines = []
tempString = []

for line in lines:
    sepLine = line.split()
    line = line.replace('\n', "")
    #Checks if tag is supported, if yes Y, if not N
    if sepLine[1] in valid_tags:
        valid_tag = "Y"
    #Cover the two exceptions, for when INDI and FAM are 3rd token/second index
    elif len(sepLine) == 3:
        if (sepLine[2] == 'INDI' or sepLine[2] == 'FAM'):
            newLines.append(tempString)
            tempString = []
    tempString += sepLine
    #Cover 2 DATE, but not 1 DATE
    if ((sepLine[0] == "2") and (sepLine[1] == "DATE")):
        valid_tag = "Y"
    #Cover 1 NAME, but not 2 NAME
    elif ((sepLine[0] == "1") and (sepLine[1] == "NAME")):
        valid_tag = "Y"
    #All other variations are not supported or valid
    else:
        valid_tag = "N"
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
childCount = {}

for line in newLines:
    _id = ""
    _famId = ""
    birth_year = 0
    deathYear = 0
    is_alive = True
    for i in range(len(line)):
        # print(line[i])
        if line [i] == "INDI":
            _id = line[i - 1]
            idList.append(_id)
        if line[i] == "FAM":
            _famId = line[i - 1]
            famIdList.append(_famId)
        if line [i] == "NAME":
            nameDic[_id] = line[i + 1] + " " + line[i + 2]
        if line[i] == "BIRT":
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
            birth_year = year
            age = 2022 - year
            ageDic[_id] = age
        if line[i] =="DEAT":
            day = ""
            month = ""
            year = ""
            death_day = ""
            if line[i + 1] == "N":
                #they're allive
                is_alive = True
                deadDic[_id] = "NA"
                aliveDic[_id] = is_alive
            elif line[i + 1] == "Y":
                is_alive = False
                aliveDic[_id] = is_alive
                #they dead
            aliveDic[_id] = is_alive
            if not is_alive:
                day = line[i + 4]
                month = line[i + 5]
                year  = line[i + 6]
                deathYear = int(year)
                age = deathYear - birth_year
                ageDic[_id] = age
                death_day = f'{month}/{day}/{year}'
                deadDic[_id] = death_day
        if is_alive:
            is_alive = True
            deadDic[_id] = "NA"
            aliveDic[_id] = is_alive
        if line[i] == "SEX":
            genderDic[_id] = line[i + 1]
        if line[i] == "CHIL":
            childDic[line[i + 1]] = _famId
        if (line[i] == "WIFE" or line[i] == "HUSB"):
            spouseDic[line[i + 1]] = _famId
            if line[i] == "WIFE":
                wifeDic[_famId] = line[i + 1]
            else:
                husbandDic[_famId] = line[i + 1]
        if line[i] == "MARR":
            day = line[i + 3]
            month = line[i + 4]
            year = line[i + 5]
            date = f"{month}/{day}/{year}"
            marriedDic[_famId] = date
        if line[i] == "DIV":
            day = line[i + 3]
            month = line[i + 4]
            year = line[i + 5]
            date = f"{month}/{day}/{year}"
            print(date)
            divorcedDic[_famId] = date
        #now the person is complete

x = PrettyTable()
x.field_names = ["ID",
                "NAME",
                "GENDER",
                "BIRTHDAY",
                "AGE", 
                "ALIVE",
                "DEATH",
                "CHILD",
                "SPOUSE"]

for id in idList:
    if not childDic.get(id):
        childDic[id] = "NA"
    if not spouseDic.get(id):
        spouseDic[id] = "NA"
    newRow = [id,nameDic.get(id),genderDic.get(id),birthDayDic.get(id),ageDic.get(id),aliveDic.get(id), deadDic.get(id), childDic.get(id), spouseDic.get(id)]
    x.add_row(newRow)
print(x)
y = PrettyTable()
y.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND NAME", "HUSBAND ID", "WIFE NAME", "WIFE ID", "CHILDREN"]
for famId in famIdList:
    childCount[famId] = 0
    if not marriedDic.get(famId):
        marriedDic[famId] = "NA"
    if not divorcedDic.get(famId):
        divorcedDic[famId] = "NA"
    children = []
    for childId in childDic:
        if childDic[childId] == famId:
            children.append(childId)
            childCount[famId] = childCount.get(famId) + 1
    newRow = [famId, marriedDic.get(famId), divorcedDic.get(famId), nameDic.get(husbandDic.get(famId)), husbandDic.get(famId), nameDic.get(wifeDic.get(famId)), wifeDic.get(famId), children]
    y.add_row(newRow)
print(y)
f.close()

#VALIDATION FOR INDIVIDUALS
for id in idList:
    birthday = birthDayDic.get(id)
    deathday = deadDic.get(id)
    age = ageDic.get(id)
    validDeathBeforeBirth = testBirthBeforeDeath(birthday, deathday)
    validAge = ageLessThanOneFifty(age)

    #SPRINT ONE
    if not validDeathBeforeBirth:
        print(f'ERROR: INDIVIDUAL: US03: {id}: Birthday {birthday} occurs before death date {deathday}')

    #SPRINT TWO
    if not validAge:
        print(f'ERROR: INDIVIDUAL: US10: {id}: Death date {deathday} occurs greater than 150 years after {birthday}')

#VALIDATION FOR FAMILIES
for id in famIdList:
    marriage = marriedDic.get(id)
    divorce = divorcedDic.get(id)
    wifeId = wifeDic.get(id)
    husbandId = husbandDic.get(id)
    birthDays = [birthDayDic.get(wifeId), birthDayDic.get(husbandId)]
    deaths = [deadDic.get(wifeId), deadDic.get(husbandId)]
    childCounter = childCount.get(id)

    validBirthMarriage = testBirthBeforeMarriage(marriage, birthDays)
    validDeathMarriage = testMarriageBeforeDeath(marriage, deaths)
    validMarriageDivorce = testMarriageBeforeDivorce(marriage,divorce)
    validDivorceDeath = testDivorceBeforeDeath(divorce, deaths)
    validChildCount = fewerThan5Kids(childCounter)
    validMarriageAges = marriageAfterYears(birthDays, marriage)

    #SPRINT ONE
    if not datesBeforeToday(marriage):
        print(f'ERROR: FAMILY: US01: {id}: Marriage date {marriage} is in the future')
    if not datesBeforeToday(divorce):
        print(f'ERROR: FAMILY: US01: {id}: Divorce date {divorce} is in the future')
    if not datesBeforeToday(birthDays[0]):
        print(f'ERROR: FAMILY: US01: {id}: Wifes birth date {birthDays[0]} is in the future')
    if not datesBeforeToday(birthDays[1]):
        print(f'ERROR: FAMILY: US01: {id}: Husbands birth date {birthDays[1]} is in the future')
    if not datesBeforeToday(deaths[0]):
        print(f'ERROR: FAMILY: US01: {id}: Wifes birth date {deaths[0]} is in the future')
    if not datesBeforeToday(deaths[1]):
        print(f'ERROR: FAMILY: US01: {id}: Husbands death date {deaths[1]} is in the future')

    if validBirthMarriage == -1:
        print(f'ERROR: FAMILY: US02: {id}: Wifes birth date {birthDays[0]} following marriage date {marriage}')
    if validBirthMarriage == -2:
        print(f'ERROR: FAMILY: US02: {id}: Husbands birth date {birthDays[1]} following marriage date {marriage}')
    if not validMarriageDivorce:
        print(f'ERROR: FAMILY: US04: {id}: Marriage Date {marriedDic.get(id)} before divorce date {divorcedDic.get(id)}')
    if validDeathMarriage == -1:
        print(f'ERROR: FAMILY: US05: {id}: Wifes death date {deaths[0]} occurs before marriage date {marriage}')
    if validDeathMarriage == -2:
        print(f'ERROR: FAMILY: US05: {id}: Husbands death date {deaths[1]} occurs before marriage date {marriage}')
    if validDivorceDeath == -1:
        print(f'ERROR: FAMILY: US06: {id}: Divorce Date {divorcedDic.get(id)} following wife death date {birthDays[0]}')
    if validDivorceDeath == -2:
        print(f'ERROR: FAMILY: US06: {id}: Divorce Date {divorcedDic.get(id)} following husbands death date {birthDays[1]}')
    
    #SPRINT TWO
    if not fewerThan5Kids(childCounter):
        print(f'ERROR: FAMILY: US07: {id}: Family has {childCount.get(id)} children, which is greater than 5.')
    if validMarriageAges == -1:
        print(f'ERROR: FAMILY: US11: {id}: Wifes birthday {birthDays[0]} is less than 18 years before marriage date {marriage}')
    if validMarriageAges == -2:
        print(f'ERROR: FAMILY: US11: {id}: Husbands birthday {birthDays[1]} is less than 18 years before marriage date {marriage}')
    for childId in childDic:
        if childDic.get(childId) == id:
            childBirthday = birthDayDic.get(childId)
            validChild9Months = childBornAfterMarriage(childBirthday, marriage)
            validChildDadDeath = fatherAliveForConception(childBirthday, deaths[1])
            validChildMomDeath = birthBeforeMotherDeath(childBirthday, deaths[0])

            if not validChild9Months:
                print(f'ERROR: FAMILY: US08: {id}: Child {childId}s birthday {childBirthday} is less than 9 months before marriage date {marriage}')
            if not validChildDadDeath:
                print(f'ERROR: FAMILY: US12: {id}: Child {childId}s birthday {childBirthday} is more than 9 months after fathers death date {deaths[1]}')
            if not validChildMomDeath:
                print(f'ERROR: FAMILY: US09: {id}: Child {childId}s birthday {childBirthday} is before mothers death date {deaths[0]}')
        

