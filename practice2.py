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

        element = driver.find_element(By.ID, "content")
        element.send_keys("Hello by Id")
        # elem = driver.find_element(By.ID, "go").click()

        element = driver.find_element(By.CSS_SELECTOR, "#description")
        element.send_keys("Hello by CSS_SEECTOR")
        element.clear()

        element = driver.find_element(By.XPATH, '//*[@id="description"]')
        element.send_keys("Hello There by Xpath")
        btn = driver.find_element(By.XPATH, '//*[@id="go"]').click()
        # element.submit()

	    #elem = driver.find_element(By.NAME, "q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
