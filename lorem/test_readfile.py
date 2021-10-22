import unittest
import readfile # importing readfiles

class Test(unittest.TestCase):
    """
    class to test the functions on the readfile module

    Argvs:
    unittest.Testcase a class from the unittest module to test the unittest
    """
    def test_get_data(self):
        """
        test case to confirm we are getting data from the test.txt file
        """
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data,readfile.readfile("test.txt"))# readfile function returns the data from the test.txt file
if __name__ == '__main__':
    unittest.main() 


