import unittest

from validate import testBirthBeforeDeath, testDivorceBeforeDeath, testMarriageBeforeDivorce
'''
function testDivorceBeforeDeath takes two inputs, 
the date of the divorce and a list of dates of the deaths of the two spouses
it returns true if the divorce date is valid and false otherwise
'''

class TestDivorce(unittest.TestCase):
    def test1(self):
        self.assertTrue(testDivorceBeforeDeath('05/20/1987', []), "Both partners are alive, should be valid")
    def test2(self):
        self.assertTrue(testDivorceBeforeDeath('05/20/1987', ['07/14/2019', '01/23/2020']), "Both partners are dead, but the divorce date should be valid")
    def test3(self):
        self.assertTrue(testDivorceBeforeDeath('04/12/1987',['07/14/2019']), "One partner is alive still, but the divorce date should be valid")
    def test4(self):
        self.assertFalse(testDivorceBeforeDeath('04/12/1987',['07/14/1980']), "One partner died before the divorce date, should be invalid")
    def test5(self):
        self.assertFalse(testDivorceBeforeDeath('04/12/1987',['07/14/1980','06/13/1980']), "Both partners died before divorce, should be invalid")
    
class TestBirthBeforeDeath(unittest.TestCase):
    def test1(self):
        self.assertTrue(testBirthBeforeDeath('03/15/2001', []))
    def test2(self):
        self.assertTrue(testBirthBeforeDeath('02/19/1935', ['05/07/2004']))
    def test3(self):
        self.assertTrue(testBirthBeforeDeath('09/04/1936',['10/18/2021']))
    def test4(self):
        self.assertFalse(testBirthBeforeDeath('01/10/1997',['06/08/1965']))
    def test5(self):
        self.assertTrue(testBirthBeforeDeath('10/01/2022',['10/02/2022']))

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

if __name__ == "__main__":
    print("Running Tests")
    unittest.main()