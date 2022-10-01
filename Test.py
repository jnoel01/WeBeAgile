import unittest

from validate import testDivorceBeforeDeath
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

if __name__ == "__main__":
    print("Running Tests")
    unittest.main();