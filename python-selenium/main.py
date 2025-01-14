from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import json
from datetime import datetime


class Scraper:
  def __init__(self, log_path="scraper.log"):
    self.setup_logging(log_path)
    self.setup_driver()

  def setup_logging(self, log_path):
    logging.basicConfig(
      filename=log_path,
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s'
    )
    self.logger = logging.getLogger(__name__)

  def setup_driver(self):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    self.driver = webdriver.Chrome(options=options)
    self.wait = WebDriverWait(self.driver, 10)

  def goto(self, url):
    try:
      self.driver.get(url)
      self.logger.info(f"Go to {url}: SUCCESS")
    except Exception as e:
      self.logger.error(f"Go to {url}: FAIL {str(e)}")

