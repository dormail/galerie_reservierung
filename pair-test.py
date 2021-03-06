""" pair-test.py
script for testing the pair function
"""

from pair import pair
from selenium import webdriver
from guest import guest

g1 = guest(1)
g1.first_name = 'max'
g1.last_name = 'mustermann'

g2 = guest(2)
g2.first_name = 'renate'

driver = webdriver.Firefox()
pair(driver, g1, g2)