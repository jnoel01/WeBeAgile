import unittest

from validate import *
'''
function testDivorceBeforeDeath takes two inputs, 
the date of the divorce and a list of dates of the deaths of the two spouses
it returns true if the divorce date is valid and false otherwise
'''

class TestDivorceBeforeDeath(unittest.TestCase):
    def test1(self):
        self.assertTrue(testDivorceBeforeDeath('05/20/1987', []), "Both partners are alive, should be valid")
    def test2(self):
        self.assertTrue(testDivorceBeforeDeath('05/20/1987', ['07/14/2019', '01/23/2020']), "Both partners are dead, but the divorce date should be valid")
    def test3(self):
        self.assertTrue(testDivorceBeforeDeath('04/12/1987',['07/14/2019']), "One partner is alive still, but the divorce date should be valid")
    def test4(self):
        self.assertEqual(testDivorceBeforeDeath('04/12/1987',['07/14/1980']),-1, "One partner died before the divorce date, should be invalid")
    def test5(self):
        self.assertEqual(testDivorceBeforeDeath('04/12/1987',['07/14/1980','06/13/1980']), -1,  "Both partners died before divorce, should be invalid")
    
class TestBirthBeforeDeath(unittest.TestCase):
    def test1(self):
        self.assertTrue(testBirthBeforeDeath('03/15/2001', ''))
    def test2(self):
        self.assertTrue(testBirthBeforeDeath('02/19/1935', '05/07/2004'))
    def test3(self):
        self.assertTrue(testBirthBeforeDeath('09/04/1936','10/18/2021'))
    def test4(self):
        self.assertFalse(testBirthBeforeDeath('01/10/1997','06/08/1965'))
    def test5(self):
        self.assertTrue(testBirthBeforeDeath('10/01/2022','10/02/2022'))

class TestMarriageBeforeDivorce(unittest.TestCase):
    def test1(self):
        self.assertTrue(testMarriageBeforeDivorce('10/20/1980', '4/4/1981'), "Marriage happened before divorce, should be valid")
    def test2(self):
        self.assertFalse(testMarriageBeforeDivorce('10/20/1981', '4/4/1970'), "Marriage happened after divorce, should be invalid")
    def test3(self):
        self.assertFalse(testMarriageBeforeDivorce('10/20/1980', '10/20/1980'), "Marriage happened the day of divorce, should be invalid. (I dont think this can happen)")
    def test4(self):
        self.assertTrue(testMarriageBeforeDivorce('10/20/1980', ''), "There was never a divorce. Should be valid.")
    def test5(self):
        self.assertTrue(testMarriageBeforeDivorce('10/20/1990', '11/4/2012'), "Marriage happened before divorce, should be valid")

class TestBirthBeforeMarriage(unittest.TestCase):
    def test1(self):
        self.assertTrue(testBirthBeforeMarriage('03/15/2001', ['09/20/1980','08/03/1976']), 'Both births are before marriage, should be valid')
    def test2(self):
        self.assertTrue(testBirthBeforeMarriage('12/1/1935', ['02/19/1935', '11/23/1935']))
    def test3(self):
        self.assertEqual(testBirthBeforeMarriage('09/04/1936',['10/18/2021', '11/03/1937']), -1,  'both births are after marriage, should be false')
    def test4(self):
        self.assertFalse(testBirthBeforeMarriage('01/10/1997',['06/08/1965']), 'Only one birth provided,should be false')
    def test5(self):
        self.assertEqual(testBirthBeforeMarriage('10/01/1980',['10/02/2022', '10/21/1970']), -1, 'one birth is after marriage, should be false')

class TestMarriageBeforeDeath(unittest.TestCase):
    def test1(self):
        self.assertTrue(testMarriageBeforeDeath('05/20/1987', []), "Both partners are alive, should be valid")
    def test2(self):
        self.assertTrue(testMarriageBeforeDeath('05/20/1987', ['07/14/2019', '01/23/2020']), "Both partners are dead, but the marriage date should be valid")
    def test3(self):
        self.assertTrue(testMarriageBeforeDeath('04/12/1987',['07/14/2019']),"One partner is alive still, but the marriage date should be valid")
    def test4(self):
        self.assertEqual(testMarriageBeforeDeath('04/12/1987',['07/14/1980']), -1,  "One partner died before the marriage date, should be invalid")
    def test5(self):
        self.assertEqual(testMarriageBeforeDeath('04/12/1987',['07/14/1980','06/13/1980']), -1,  "Both partners died before marriage, should be invalid")

class TestDatesBeforeToday(unittest.TestCase):
    def test1(self):
        self.assertTrue(datesBeforeToday('10/20/1981'), "One date before today, should be valid")
    def test2(self):
        self.assertTrue(datesBeforeToday('10/20/1981'), "should be valid")
    def test3(self):
        self.assertTrue(datesBeforeToday(''), "No dates given, should be valid")
    def test4(self):
        self.assertFalse(datesBeforeToday('10/20/2023'), "should be invalid")
    def test5(self):
        self.assertFalse(datesBeforeToday('10/20/2025'), " should be invalid")
        
class TestChildBirthBeforeMomDeath(unittest.TestCase):
    def test1(self):
        self.assertTrue(birthBeforeMotherDeath('10/01/2001', "NA"), "Mom not dead, should be valid")
    def test2(self):
        self.assertTrue(birthBeforeMotherDeath('10/01/2001', ""), "Mom not dead, should be valid")
    def test3(self):
        self.assertTrue(birthBeforeMotherDeath('10/01/2001', "10/01/2009"), "Mom dead after birth, should be valid")
    def test4(self):
        self.assertFalse(birthBeforeMotherDeath('10/01/2001', "10/08/1991"), "Mom dies before birth, should be invalid")

class TestAgeLessThanOneFifty(unittest.TestCase):
    def test1(self):
        self.assertTrue(ageLessThanOneFifty(100), "younger than 100, should pass")
    def test2(self):
        self.assertTrue(ageLessThanOneFifty(150), "is 150, should pass")
    def test3(self):
        self.assertFalse(ageLessThanOneFifty(151), "151 should fail")
    def test4(self):
        self.assertTrue(ageLessThanOneFifty(0), "infant: should pass")

class TestMarriageAfterFourteen(unittest.TestCase):
    def test1(self):
        self.assertTrue(marriageAfterYears(['9/10/1990', '5/30/1988'], '4/23/2014'), 'Should pass because both are older than 14')
    def test2(self):
        self.assertEqual(marriageAfterYears(['9/10/2004', '5/24/1970'], '4/12/2012'), -1, 'Should fail because wife is younger than 14')
    def test3(self):
        self.assertEqual(marriageAfterYears(['9/10/1980', '5/24/2005'], '4/12/2011'), -2, 'Should fail because husband is younger than 14')
    def test4(self):
        self.assertTrue(marriageAfterYears(['9/10/2004', '5/24/1970'], ''), 'Should pass because these two arent married')

class TestFewerThan5Kids(unittest.TestCase):
    def test1(self):
        self.assertTrue(fewerThan5Kids(['@01@', "@02", "@03@", "@04@", "@05" ]), "5 kids should return true")
    def test2(self):
        self.assertFalse(fewerThan5Kids(['@01@', "@02", "@03@", "@04@", "@05@", "@06@" ]), "6 kids should return false")
    def test3(self):
        self.assertTrue(fewerThan5Kids(['@01@', "@02", "@03@", "@04@", ]), "4 kids should return true")
    def test4(self):
        self.assertTrue(fewerThan5Kids([]), "0 kids should return true")

class TestChildBornAfterMarriage(unittest.TestCase):
    def test1(self):
        self.assertTrue(childBornAfterMarriage('5/20/2007', '3/12/1990'), 'Should be valid')
    def test2(self):
        self.assertFalse(childBornAfterMarriage('5/20/2008', '3/19/2008'), 'Should be invalid')
    def test3(self):
        self.assertFalse(childBornAfterMarriage('5/19/2000', '2/12/2003'), 'Should be invalid')
    def test4(self):
        self.assertTrue(childBornAfterMarriage('', '5/20/2001'), 'Should be valid')

class TestFatherAliveForConception(unittest.TestCase):
    def test1(self):
        self.assertFalse(fatherAliveForConception('5/20/2007', '3/12/1990'), 'Should be invalid')
    def test2(self):
        self.assertFalse(fatherAliveForConception('5/21/2007', '5/20/2006'), 'Father died before conception')
    def test3(self):
        self.assertTrue(fatherAliveForConception('5/20/2007', '11/20/2006'), 'Father died same day as conception :(')
    def test4(self):
        self.assertTrue(fatherAliveForConception('5/20/2007', '9/01/2008'), 'Should be valid')

if __name__ == "__main__":
    print("Running Tests")
    unittest.main()