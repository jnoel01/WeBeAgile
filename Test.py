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
        self.assertTrue(testMarriageBeforeDivorce('10/20/1980', '10/20/1980'), "Marriage happened the day of divorce, should be valid.")
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

class TestChildBornAfterMarriage(unittest.TestCase):
    def test1(self):
        self.assertFalse(childBornAfterMarriage('3/20/2001', '10/20/2000'), 'Should be invalid')
    def test2(self):
        self.assertTrue(childBornAfterMarriage('3/20/2001', '5/20/2000'), 'Should be valid')
    def test3(self):
        self.assertTrue(childBornAfterMarriage('11/4/2001', '10/5/1999'), 'Should be valid')
    def test4(self):
        self.assertFalse(childBornAfterMarriage('3/20/1999', '5/20/2001'), 'Should be invalid')
    def test5(self):
        self.assertFalse(childBornAfterMarriage('11/5/2001', '10/12/2001'), 'Should be invalid')
    def test6(self):
        self.assertTrue(childBornAfterMarriage('12/11/2001', '1/12/2001'), 'Should be valid')

class TestFatherAliveForConception(unittest.TestCase):
    def test1(self):
        self.assertTrue(fatherAliveForConception('3/20/2001', '10/20/2000'), 'Should be valid')
    def test2(self):
        self.assertFalse(fatherAliveForConception('3/20/2001', '5/20/2000'), 'Should be invalid')
    def test3(self):
        self.assertFalse(fatherAliveForConception('3/19/2001', '10/12/1999'), 'Should be valid')
    def test4(self):
        self.assertTrue(fatherAliveForConception('3/20/1999', '5/20/2001'), 'Should be valid')
    def test5(self):
        self.assertTrue(fatherAliveForConception('3/11/2001', '1/12/2001'), 'Should be valid')
    def test6(self):
        self.assertFalse(fatherAliveForConception('12/11/2001', '1/12/2001'), 'Should be invalid')

class maxSiblingBirth(unittest.TestCase):
    def test1(self):
        self.assertTrue(maxSiblingBirth(5, ['11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020']), 'Should be valid')
    def test2(self):
        self.assertFalse(maxSiblingBirth(6, ['11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020']),  'Should be invalid')
    def test3(self):
        self.assertFalse(maxSiblingBirth(6, ['11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2021']), 'Should be valid')
    def test4(self):
        self.assertTrue(maxSiblingBirth(1, ['06/12/1999']), 'Should be valid')
    def test5(self):
        self.assertTrue(maxSiblingBirth(0, []), 'Should be valid')
    def test6(self):
        self.assertFalse(maxSiblingBirth(10, ['11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020', '11/12/2020']), 'Should be invalid')

class maxSiblingsTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(maxSiblings(5), "5 kids should return true")
    def test2(self):
        self.assertFalse(maxSiblings(16), "6 kids should return false")
    def test3(self):
        self.assertTrue(maxSiblings(0), "4 kids should return true")
    def test4(self):
        self.assertTrue(maxSiblings(15), "0 kids should return true")
class testCantMarryChildren(unittest.TestCase):
    def test1(self):
        self.assertTrue(cantMarryChild('A1', 'B2', []), "no kids should pass")
    def test2(self):
        self.assertTrue(cantMarryChild('A1', '', []), "not married should pass")
    def test3(self):
        self.assertTrue(cantMarryChild('', '', []), 'empty family should pass')
    def test3(self):
        self.assertFalse(cantMarryChild('A1', 'B2', ['B2']), '1 child married should fail - dad incest')
    def test4(self):
        self.assertFalse(cantMarryChild('A1', 'B2', ['A1' ]), '1 child married should fail - mom incest')
    def test5(self):
        self.assertFalse(cantMarryChild('A1', 'B2', ['A1', 'D3', 'D5' ]), '1 child married should fail - dad incest with multiple kids')
    def test6(self):
        self.assertTrue(cantMarryChild('A1', 'B2', ['D1', 'D3', 'D5' ]), 'valid family with kids should pass')
        
class testCantMarrySibling(unittest.TestCase):
    testDict = {'F1': ['A1', 'A2', 'A3'],'F2': ['B1', 'B2'],'F3': ['C1', 'C2', 'C3', 'C4']}
    def test1(self):
        self.assertTrue(cantMarrySibling('A1', 'B2', {}), 'no children in famToChildren should pass')
    def test2(self):
        self.assertTrue(cantMarrySibling("A1", "",{}), 'only 1 spouse, should pass')
    def test3(self):
        self.assertTrue(cantMarrySibling("", "",{}), 'no spouse and no chidlren should pass')
    def test3(self):
        self.assertTrue(cantMarrySibling("A1", "B4",self.testDict), 'valid marriage should pass')
    def test4(self):
        self.assertFalse(cantMarrySibling("A1", "A2",self.testDict), '2 of 3 children married should fail')
    def test5(self):
        self.assertFalse(cantMarrySibling("B1", "B2",self.testDict), '2 of 2 children married should fail')

if __name__ == "__main__":
    print("Running Tests")
    unittest.main()