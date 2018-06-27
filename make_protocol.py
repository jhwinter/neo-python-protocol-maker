#!/usr/bin/env python

import re
import time

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys  # didn't need this stuff
#from bs4 import BeautifulSoup, SoupStrainer

from .make_json import write_to_json

def main():
    """
    This method opens the browser, gets all functional nodes, picks the very best amongst them,
    and adds them to the protocol.json file
    :return:
    """
    try:
        browser = webdriver.Chrome()
    except:
        browser = webdriver.Firefox()  # haven't tested with this

    url = "http://monitor.cityofzion.io/"
    browser.get(url)  # navigates to the url and waits for it to fully load

    time.sleep(10)  # you only get like 1 node if you don't give the page time to ping the nodes again
    possible_seed_list = []
    rows = browser.find_elements_by_class_name('color-success')  # gets all table rows with class='color-success'
    for row in rows:  # converting all rows from webdriver elements to strings
        possible_seed_list.append(row.text)

    # the following is a crude implementation, but I'm not too great with regular expressions
    # so feel free to modify this to be more efficient
    seed_list = []
    for row in possible_seed_list:
        row = row.replace('\n', ' ').split(' ')
        if row[0].endswith('10332') and int(row[2]) < 250:
            row[0] = row[0].split('://')  # remove http/https from url
            row[0][1] = row[0][1].split(':')  # remove '10332' port from url
            seed = row[0][1][0] + ':10333'  # append the 10333 port to the url
            seed_list.append(seed)

    fp = '../neo-python/neo/data/protocol.mainnet.json'
    write_to_json(seed_list, fp)
    print("end>>>>>>>>>>>>>")
    return True


if __name__ == "__main__":
    main()
