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



def getDistanceBetweenDates(a,b):
    #takes two dates and returns the length between as 
    # a list of [years, months, days]
    if (a == "NA" or b == "NA"):
        return True
    result = []
    result[0] = b[2] - a[2]
    if b[0] >= a[0]:
        result[1] = b[0] - a[0]
    else:
        result[0] = result[0] - 1
        result[1] = 12 - a[0] + b[0]
    if b[1] >= a[1]:
        result[2] = b[1] - a[1]
    else:
        result[2] = 31 - a[1] + b[1]
    return result


def formatDate(date):
    if (date == "NA" or not date):
        return "NA"
    list = date.split("/")
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
    if b[2] < a[2]: return False
    elif b[2] == a[2] and b[0] < a[0]: return False
    elif b[2] == a[2] and b[0] == a[0] and b[1] < a[1]: return False
    else: return True 



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

#after refactoring 
def fatherAliveForConception(childBorn, fatherDeath):
    if(fatherDeath == "NA"):
        #father must be alive during child conception
        return True 
    if (not childBorn or not fatherDeath):
        return True
    if len(childBorn) == 0 or len(fatherDeath) == 0:
        return True
    childBorn = formatDate(childBorn)
    fatherDeath = formatDate(fatherDeath)
    #format birth into conception, check against father's death
    conception = childBorn
    for i in range(9):
        if conception[0] != 1:
            conception[0] = conception[0] - 1
        else:
            conception[0] = 12
            conception[2] = conception[2] - 1
    return compareDate(conception,fatherDeath)    



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

def maxSiblingBirth(birthday, children):
    if children == 5:
        for child in len(children):
            if birthday[child].get() ==  birthday[child-1].get():
                ++child 
                return False
            else:
                return True
    else:
        return True

def maxSiblings(kids, num):
    if kids > num:
        return False
    else:
        return True

def cantMarryChild(fatherId, motherId, children):
    #takes two the family's spouse ID's and an array of their children 
    #returns true if no incest 
    result = True
    if motherId == fatherId: return False
    if not fatherId or not motherId: return True
    for child in children:
        if (fatherId == child or motherId == child):
            result = False
    return result

def cantMarrySibling(husbandId, wifeId, dict):
    # takes two spouse's id's and their family ID
    result = True
    children = []
    for fam in dict:
        children = fam
        if husbandId in children and wifeId in children:
            result = False
            return False
    return result

def cantMarryFamily(husband, wife, members):
    if husband in members:
        return False
    else:
        return True

def antiFiveBirths(birthdays):
    if len(birthdays) < 0:
        return True
    diction = {}
    for day in birthdays:
        if not diction.get(day):
            diction[day] = 1
        else:
            diction[day] = diction.get(day) + 1
    for val in diction:
        if diction.get(val) > 5:
            return False
    return True
        


testDict = {'F1': ['A1', 'A2', 'A3'],'F2': ['B1', 'B2'],'F3': ['C1', 'C2', 'C3', 'C4']}
cantMarryChild('C1', 'C2', testDict)

    
