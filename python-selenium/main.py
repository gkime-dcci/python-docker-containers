import os
from getpass import getpass
from enum import Enum
import logging
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# SELENIUM RESOURCES:
# FINDING DOM ELEMENTS https://www.selenium.dev/documentation/webdriver/elements/locators/


class ResourceType(Enum):
  # INSERT RESOURCE TYPES HERE
  # EXAMPLE: 
  DOCUMENT = "DOCUMENT"

class LocatorType(Enum):
  className = "className"
  cssSelector = "cssSelector"


class Scraper:
  def __init__(self, url=None, output_path=None, log_path="scraper.log"):
    self.setup_logging(log_path)
    self.setup_driver()
    self.url = url
    self.output_path = output_path
    

  def setup_logging(self, log_path):
    logging.basicConfig(
      filename=log_path,
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s'
    )
    self.logger = logging.getLogger(__name__)

  def setup_driver(self):
    driver_path= os.getenv('CHROME_BIN')
    options = webdriver.ChromeOptions()
    chosen_options = os.getenv('CHROME_OPTIONS', '').split()
    for option in chosen_options:
      options.add_argument(option)
    service = webdriver.ChromeService(service=driver_path)
    self.driver = webdriver.Chrome(service, options=options)
    self.wait = WebDriverWait(self.driver, 10)

  def goto(self, url):
    if self.url is None:
      self.url = url
    try:
      self.driver.get(url)
      self.logger.info(f"Go to {url}: SUCCESS")
    except Exception as e:
      self.logger.error(f"Go to {url}: FAIL {str(e)}")

  def authWithLogin(self):
    if self.auth is None:
      return
    
  def locate_element_by(self, locator: LocatorType, locator_arg: str):
    self.driver.find_element(getattr(By, locator), locator_arg)

    
  def save_data(self, resource, resource_type, filename=None):
    if filename is None:
      filename = f"scraped_{resource_type}_{datetime.now()}.json"

it_glue_scraper = Scraper(url="https://www.itglue.com/", output_path="./")
it_glue_scraper.goto(it_glue_scraper.url)
it_glue_scraper.locate_element_by(LocatorType.className, "hi")