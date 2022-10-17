# file used to validate logic in parser.py
from datetime import *
from sqlite3 import connect

dateDic = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}


def formatDate(date):
    if (date == "NA" or not date):
        return "NA"
    list = date.split("/")
    #print(list)
    if not dateDic.get(list[0]):
        result = [int(list[0]), int(list[1]), int(list[2])]
    else:
        result = [dateDic.get(list[0]), int(list[1]), int(list[2])]
    return result
def compareDate(a,b):
    #returns true if B is after A
    #if b is the same day as A, it also returns true
    if (a == "NA" or b == "NA"):
        return True
    if b[2] > a[2]: #year b is after a
        return True
    elif b[2] == a[2]: #same year
        if b[0] > a[0]: #month b is after a
            return True
        elif b[0] == a[0]: #same year same month
            if b[1] > a[1]:#day b is after a
                return True
            elif b[1] == a[1]:
                return True
            else: #day b is before a
                return False
        else:
            return False
    else: # year b is before a
        return False
def datesBeforeToday(dates):
    valid = True
    today = date.today()
    today = today.strftime('%m/%d/%Y')
    today = formatDate(today)
    dates = formatDate(dates)
    if len(dates) == 0:
        return valid
    if not compareDate(dates, today):
        valid = False
    return valid

def testDivorceBeforeDeath(divorce, deaths):
    count = 0
    valid = True
    if not divorce:
        return True
    if len(deaths) == 0:
        return valid
    divorce = formatDate(divorce)
    for death in deaths:
        death = formatDate(death)
        if not compareDate(divorce,death):
            if count == 0:
                return -1
            else:
                return -2
        count = count + 1
    return valid

def testBirthBeforeDeath(birth, deathDate):
    #takes 1 birth date and death date as a string and returns true if its valid
    if not deathDate:
        return True
    valid = True
    birth = formatDate(birth)
    deathDate = formatDate(deathDate)
    if not compareDate(birth,deathDate):
        valid = False
    return valid

def testMarriageBeforeDivorce(marriage, divorce):
    valid = True
    if(marriage == divorce) or (marriage == "NA"):
        return True
    if not divorce:
        return valid
    divorce = formatDate(divorce)
    marriage = formatDate(marriage)
    if not compareDate(marriage, divorce):
        valid = False
    return valid

def testBirthBeforeMarriage(marriage, births):
    #takes 1 marriage date and list of spouses' births,
    #returns true if both births are before marriage
    count = 0
    valid = True
    if len(births) != 2:
        valid = False
    marriage = formatDate(marriage)
    for birth in births:
        birth = formatDate(birth)
        if not compareDate(birth,marriage):
            if count == 0:
                return -1
            else:
                return -2
        count = count + 1
    return valid 

def testMarriageBeforeDeath(marriage, deaths):
    #takes 1 marriage date and a list of death dates, returns true if the dates are valid
    count = 0
    valid = True
    if len(deaths) == 0:
        return valid
    marriage = formatDate(marriage)
    for death in deaths:
        death = formatDate(death)
        if not compareDate(marriage,death):
            if count == 0:
                return -1
            else:
                return -2
        count = count + 1
    return valid


def birthBeforeMotherDeath(childBirth, motherDeath):
    #takes birth and death and checks that the birth comes before mom's death
    if (motherDeath == "NA" or not motherDeath):
        #mom is alive so its cool
        return True
    childBirth = formatDate(childBirth)
    motherDeath = formatDate(motherDeath)
    valid = compareDate(childBirth, motherDeath)
    return valid

def ageLessThanOneFifty(age):
    #Death should be less than 150 years after birth
    #So max age is 150
    if age <= 150:
        return True
    else:
        return False

def marriageAfterYears(births, marriage):
    #ensures that the marriage date of two people is after 18 years
    count = 0
    if (not marriage or marriage == "NA"):
        return True
    marriage = formatDate(marriage)
    for birth in births:
        birth = formatDate(birth)
        if marriage[2] - birth[2] < 0:
            return 1
        if marriage[2] - birth[2] < 18:
            if count == 0:
                return -1
            else:
                return -2
        count = count + 1
    return True

def fewerThan5Kids(kids):
    #checks if number of kids inputted is less than 5
    if kids <= 5:
        return True
    else:
        return False

def fatherAliveForConception(childBorn, fatherDeath):
    #father must be alive during child conception
    if(fatherDeath == "NA"):
        return True #Child is born to parents who aren't married
    if (not childBorn or not fatherDeath):
        return True
    if len(childBorn) == 0 or len(fatherDeath) == 0:
        return True
    childBorn = formatDate(childBorn)
    fatherDeath = formatDate(fatherDeath)
    if(childBorn[2] - fatherDeath[2] >= 2):
        return False
    elif (childBorn[2] - fatherDeath[2] < 0):
        return True
    elif(childBorn[2] - fatherDeath[2] == 1):
        threshold = 9 - childBorn[0]
        if(12 - fatherDeath[0] > threshold):
            return False
        else:
            return True
    else:
        if(childBorn[0] - fatherDeath[0] > 9):
            return False
        else:
            return True


def childBornAfterMarriage(childBorn, marriageDate):
    if(marriageDate == "NA"):
        return True #Child is born to parents who aren't married
    if (not childBorn or not marriageDate):
        return True
    if len(childBorn) == 0 or len(marriageDate) == 0:
        return True
    childBorn = formatDate(childBorn)
    marriageDate = formatDate(marriageDate)
    if(childBorn[2] - marriageDate[2] >= 2):
        return True
    elif (childBorn[2] - marriageDate[2] < 0):
        return False
    elif(childBorn[2] - marriageDate[2] == 1):
        threshold = 9 - childBorn[0]
        if(12 - marriageDate[0] > threshold):
            return True
        else:
            return False
    else:
        if(childBorn[0] - marriageDate[0] > 9):
            return True
        else:
            return False
            
