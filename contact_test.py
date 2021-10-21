import unittest # import the unittest module
from contact import Contact # importing the contact from the contact class

class TestContact(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    """
#items up here 
#creating a contact
def setUp(self):
    """
    set up the test to run before each test cases
    """
    self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com")#create contact object
def test_init_contact(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_contact.first_name,"James")# self.assertEqual checks for the an expected results
    self.assertEqual(self.new_contact.last_name,"Muriuki")# self.assertEqual checks for the an expected results
    self.assertEqual(self.new_contact.number,"0712345678")# self.assertEqual checks for the an expected results
    self.assertEqual(self.new_contact.email,"james@ms.com")# self.assertEqual checks for the an expected results

if __name__=="__main__":  
    unittest.main() #provides a command line interface that collects all the tests methods and executes them.

#saving a contact

def test_save_contact(self):
    """
     test_save_contact test case to test if the contact object is saved into
         the contact list
    """
      
    self.new_contact.save_contact()#saving a new contact
    self.assertEqual(len(Contact.contact_list), 1)

if __name__ == '__main__':
    unittest.main()  

#saving the contact
def test_save_contact(self):
    """
     test_save_contact test case to test if the contact object is saved into
         the contact list
    """
    self.new_contact.save_contact()#saving a new contact
    self.assertEqual(len(Contact.contact_list),1)
if __name__=='__main__':
    unittest.main()


