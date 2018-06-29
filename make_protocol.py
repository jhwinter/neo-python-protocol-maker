#!/usr/bin/env python

import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


from make_json import write_to_json


def main():
    """
    This method opens the browser, gets all functional nodes, picks the very best amongst them,
    and adds them to the protocol.json file
    :return:
    """
    browser = None
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        print('using chrome')
    except:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--window-size=1420,1080')
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        browser = webdriver.Firefox(firefox_options=firefox_options)
        print('using firefox')

    url = 'http://monitor.cityofzion.io/'
    browser.get(url)  # navigates to the url and waits for it to fully load

    time.sleep(10)  # you only get like 1 node if you don't give the page time to ping the nodes again
    possible_seed_list = []
    rows = browser.find_elements_by_class_name('color-success')  # gets all table rows with class='color-success'
    for row in rows:  # converting all rows from webdriver objects to strings
        possible_seed_list.append(row.text)

    # the following is a crude implementation, but I'm not too great with regular expressions
    # so feel free to modify this to be more efficient
    seed_list = []
    for row in possible_seed_list:
        row = row.replace('\n', ' ').split(' ')  # make the formatting more consistent in each row
#        search_url = re.search(r'http(.*)binding">(.*?):10332', row, re.M | re.I)
#        if search_url and int(row[2]) < 250 and len(seed_list) < 5:
#            seed_list.append(search_url.group(2)+':10333')
#        else:
#            break
        if row[0].endswith('10332') and int(row[2]) < 250 and len(seed_list) < 5:  # only choose nodes that follow the neo standard and have a ping of less than 250 ms
            row[0] = row[0].split('://')  # remove http/https from url
            row[0][1] = row[0][1].split(':')  # remove '10332' port from url
            seed = row[0][1][0] + ':10333'  # append the 10333 port to the url
            seed_list.append(seed)
        else:
            break

    fp = '../neo-python/neo/data/protocol.mainnet.json'
    write_to_json(seed_list, fp)
    print('neo-python SeedList has been updated')
    browser.close()
    return True
