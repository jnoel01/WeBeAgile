from datetime import date
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
    "DEC": 12
}


def formatDate(date):
    if (date == "NA") or not(date):
        return "NA"
    list = date.split("/")
    #print(list)
    result = [dateDic.get(list[0]), int(list[1]), int(list[2])]
    return result
    # for i in range(len(list)):

    #     list[i] = int(list[i])
    # return list

def compareDate(a,b):
    if (a == "NA") or (b == "NA"):
        return True
    #returns true if B is after A
    #if b is the same day as A, it also returns true
    if b[2] > a[2]: #year b is after a
        return True
    elif b[2] == a[2]: #same year
        if (b[0] > a[0]): #month b is after a
            return True
        elif (b[0] == a[0]): #same year same month
            if (b[1] > a[1]):#day b is after a
                return True
            elif (b[1] == a[1]):
                return True
            else: #day b is before a
                return False
        else:
            return False
    else: # year b is before a
        return False
    
def testDivorceBeforeDeath(divorce, deaths):
    count = 0
    valid = True 
    if not(divorce):
        return True
    if (len(deaths) == 0):
        return valid
    divorce = formatDate(divorce)
    for death in deaths:
        death = formatDate(death)
        if not(compareDate(divorce,death)):
            if(count == 0):
                return -1
            else:
                return -2
        count = count + 1
    return valid

def testBirthBeforeDeath(birth, deathDate):
    #takes 1 birth date and death date as a string and returns true if its valid
    valid = True 
    if (len(deathDate) == 0):
        return valid
    birth = formatDate(birth)
    deathDate = formatDate(deathDate)
    if not(compareDate(birth,deathDate)):
        valid = False
    return valid

def testMarriageBeforeDivorce(marriage, divorce):
    valid = True
    if(marriage == divorce):
        return False
    if not divorce:
        return valid
    divorce = formatDate(divorce)
    marriage = formatDate(marriage)
    if not(compareDate(marriage, divorce)):
        valid = False
    return valid

def testBirthBeforeMarriage(marriage, births):
    count = 0
    #takes 1 marriage date and list of spouses' births, returns true if both births are before marriage
    valid = True 
    if (len(births) != 2):
        valid = False
    marriage = formatDate(marriage)
    for birth in births:
        birth = formatDate(birth)
        if not(compareDate(birth,marriage)):
            if(count == 0):
                return -1
            else:
                return -2
        count = count + 1
    return valid 
    
def testMarriageBeforeDeath(marriage, deaths):
    #takes 1 marriage date and a list of death dates, returns true if the dates are valid
    valid = True 
    if (len(deaths) == 0):
        return valid
    marriage = formatDate(marriage)
    for death in deaths:
        death = formatDate(death)
        if not(compareDate(marriage,death)):
            valid = False
            break
    return valid

def datesBeforeToday(dates):
    valid = True
    today = date.today()
    today = today.strftime('%m/%d/%Y')
    today = formatDate(today)
    dates = formatDate(dates)
    if(len(dates) == 0):
        return valid
    if not(compareDate(dates, today)):
        valid = False
    return valid
    

