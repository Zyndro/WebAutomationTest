import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class CalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create a new Firefox session
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://ahfarmer.github.io/calculator/")

    def numberSelect(self,x):
        x = self.driver.find_element(By.XPATH, '//button[text()="'+str(x)+'"]')
        x.click()

    def numberAdd(self):
        x = self.driver.find_element(By.XPATH, '//button[text()="+"]')
        x.click()

    def numberEqual(self):
        x = self.driver.find_element(By.XPATH, '//button[text()="="]')
        x.click()

    def result(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div').text

    # Tests:

    def test_Addition(self):
        self.numberSelect(7)
        self.numberAdd()
        self.numberSelect(8)
        self.numberEqual()
        self.assertEqual(self.result(),"15")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    log_file = 'CalculatorTestResults.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
