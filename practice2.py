import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        self.assertIn("DB", driver.title)
        # self.assertIn("Forum", driver.h1)

        element = driver.find_element(By.ID, "content")
        element.send_keys("Hello")
        # elem = driver.find_element(By.ID, "go").click()
        element.submit()



	    #elem = driver.find_element(By.NAME, "q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
