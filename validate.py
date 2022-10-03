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
    valid = True 
    if (len(deathDate) == 0):
        return valid
    birth = formatDate(birth)
    for death in deathDate:
        death = formatDate(death)
        if not(compareDate(birth,death)):
            valid = False
            break
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


print(testDivorceBeforeDeath('05/20/1987', ['07/14/2019', '01/23/2020']))
print(testBirthBeforeDeath('08/15/1987', ['08/14/1987']))
print(testMarriageBeforeDivorce('10/20/1980', '10/20/1980'))