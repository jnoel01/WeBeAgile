from datetime import date

def formatDate(date):
    list = date.split("/")
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def compareDate(a,b):
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
    valid = True 
    if (len(deaths) == 0):
        return valid
    divorce = formatDate(divorce)
    for death in deaths:
        death = formatDate(death)
        if not(compareDate(divorce,death)):
            valid = False
            break
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
    if(len(divorce) == 0):
        return valid
    divorce = formatDate(divorce)
    marriage = formatDate(marriage)
    if not(compareDate(marriage, divorce)):
        valid = False
    return valid

def testBirthBeforeMarriage( marriage, births):
    #takes 1 marriage date and list of spouses' births, returns true if both births are before marriage
    valid = True 
    if (len(births) != 2):
        valid = False
    marriage = formatDate(marriage)
    for birth in births:
        birth = formatDate(birth)
        if not(compareDate(birth,marriage)):
            valid = False
            break
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
    if(len(dates) == 0):
        return valid
    for el in dates:
        el = formatDate(el)
        if not(compareDate(el, today)):
            valid = False
            break
    return valid
    

