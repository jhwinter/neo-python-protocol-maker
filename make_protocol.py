#!/usr/bin/env python

import time
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from make_json import write_to_json


def get_key(seed):
    """
    This method returns the integer value of the node's latency to be used as the key for sorting the nodes in
    the seed list
    :param seed: the seed from the seed list
    :return: integer value of the seed's latency
    """
    return int(seed[2])


if __name__ == '__main__':
    """
    This method opens the browser, gets all functional nodes, sorts the list of nodes by latency,
    and adds five of them to the protocol.json file
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

    possible_seed_list = list(map(lambda seed: seed.split(' '), possible_seed_list))
    possible_seed_list = sorted(possible_seed_list, key=get_key)  # sort the seed list by latency
    # the following is a crude implementation, but I'm not too great with regular expressions
    # so feel free to modify this to be more efficient
    seed_list = []
    for row in possible_seed_list:
        if row[0].endswith(':10332') and len(seed_list) < 5 and row[1] == 'RPC':  # only choose nodes that follow the neo standard
            seed = urlparse(row[0]).netloc  # returns only the url part of the string such as: seed4.travala.com:10332
            seed = seed.replace('10332', '10333')  # connect to the P2P port instead of the RPC port
            print('seed: ', seed)
            seed_list.append(seed)

    fp = 'neo-python/neo/data/protocol.mainnet.json'
    if len(seed_list) > 0:
        write_to_json(seed_list, fp)
        print('neo-python SeedList has been updated')
        browser.close()
    else:
        print('neo-python SeedList has not been updated')
        browser.close()
