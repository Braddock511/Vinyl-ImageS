from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
from statistics import median
from re import sub, findall
from pandas import DataFrame
from numpy import array
from re import sub, findall

class Scraper:
    def __init__(self, path_website: str, cookie: str):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('log-level=3')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        self.driver.get(path_website)

        sleep(2)
        try:
            self.driver.find_element(By.ID, cookie).click()
        except:
            self.driver.find_element(By.CLASS_NAME, cookie).click()

        self.error = []
        self.results = []
        self.info = []
        self.output = []

        self.conditions = {'M':'Mint (M)', 'MINT, FOLIA':'Mint (M)', "MINT. NOWA ZAFOLIOWANA": 'Mint (M)',
        '-M':'Near Mint (NM or M-)', 'M-':'Near Mint (NM or M-)', 'MINT-':'Near Mint (NM or M-)', '-MINT':'Near Mint (NM or M-)', 'MINT-.':'Near Mint (NM or M-)', 'MINT-.DO UMYCIA':'Near Mint (NM or M-)',
        'EX':'Near Mint (NM or M-)', 'EX+':'Near Mint (NM or M-)', 'EX++':'Near Mint (NM or M-)', 'EX-':'Near Mint (NM or M-)', 'EX.':'Near Mint (NM or M-)', 'EXCELLENT':'Near Mint (NM or M-)',
        'VG':'Very Good (VG)', 'VG-':'Very Good (VG)', 'VERY GOOD':'Very Good (VG)', 'DOBRY':'Very Good (VG)',
        'VG+':'Very Good Plus (VG+)', 'VG++':'Very Good Plus (VG+)', 'BARDZO DOBRY':'Very   Good Plus (VG+)', 'BARDZO DOBRY.':'Very Good Plus (VG+)',  'BARDZO DOBRY.PŁYTA DO UMYCIA':'Very Good Plus (VG+)', 'BARDZO DOBRY.DROBNE RYSKI':'Very Good Plus (VG+)', 'BARDZO DOBRY.DO UMYCIA':'Very Good Plus (VG+)',
        'G':'Good (G)', 'GOOD': 'Good (G)', 'GOOD+': 'Good (G)', }

        self.to_polish = {'M': 'Nowy', '-M':'Prawie idealny', 'VG+':'Bardzo dobry', "VG":'Calkiem dobry', 'G':'Dobry'}

    def find(self, barcode: str, index: int):
        self.barcode = barcode

        try:
            self.driver.find_element(By.ID, 'search_q').send_keys(barcode)
            self.driver.find_element(By.ID, 'do_site_search').click()
            self.driver.find_elements(By.CLASS_NAME, 'thumbnail_center')[index].click()
        except NoSuchElementException:
            try:
                self.driver.find_element(By.NAME, 'q').send_keys(barcode)
                self.driver.find_element(By.CLASS_NAME, 'submit_1SQ5c').click()
                self.driver.find_elements(By.CLASS_NAME, 'thumbnail_center')[index].click()
            
            except NoSuchElementException:
                return False

            except ElementClickInterceptedException:
                self.driver.execute_script("window.scrollBy(0, 800);")
                sleep(.5)
                try:
                    self.driver.find_elements(By.CLASS_NAME, 'thumbnail_center')[index].click()
                except IndexError:
                    return False
            
            except IndexError:
                return False

        except IndexError:
            return False   

        return True         
            
    def get_price(self, m_condition: str):
        try:
            prices = self.driver.find_element(By.CLASS_NAME, "forsale_QoVFl")
            prices.find_element(By.CLASS_NAME, 'link_1ctor').click()
        except NoSuchElementException:
            pass

        try:
            self.driver.find_element(By.XPATH, "//span[text()='Price']").click()
        except NoSuchElementException:
            return 0

        self.exists_flag = False
        self.m_condition = m_condition
        self.price = 0
        item = None

        m_condition = self.conditions.get(m_condition)

        try:
            filter_condition = self.driver.find_element(By.CLASS_NAME, "filter_condition ")
            filter_condition.find_element(By.XPATH, f"//span[text()='{m_condition}']").click()
        except (NoSuchElementException, ElementClickInterceptedException):
            pass

        
        self.nav = self.driver.find_elements(By.CSS_SELECTOR, ".shortcut_navigable")
        list_of_prices = []

        for element in self.nav:
            element = element.text
            try:
                if f'Media Condition: {m_condition}' in element:
                    item_euro = findall(r'€.*', element)[0]
                    item = sub('€', '', item_euro)

                    if not item or 'total' in item:
                        try:
                            item_dolar = findall(r'\$.*', element)[0]
                            item = sub('\$', '', item_dolar)
                        except IndexError:
                            pass

                    if not item or 'total' in item:
                        try:
                            item_pound = findall(r'£.*', element)[0]
                            item = sub('£', '', item_pound)
                        except IndexError:
                            pass

                    if not item or 'total' in item:
                        try:
                            item_swiss_pound = findall(r'CHF.*', element)[0]
                            item = sub('CHF', '', item_swiss_pound)
                        except IndexError:
                            pass

                    if not 'total' in item:
                        self.price = float(item) * 4.6
                        list_of_prices.append(self.price)
                        self.exists_flag = True
            except ValueError:
                pass     
                
        if self.exists_flag:
            self.price = median(list_of_prices)       
            self.price = round(self.price, -1)-0.01
            if self.price <= 0:
                self.price = 9.99

        return self.price

    def quit(self):
        self.driver.quit()

    def url(self, url: str):
        self.driver.get(url)