from time import sleep
from datetime import datetime
import random

from splinter import Browser

USERNAME = ''
PASSWORD = ''

# wait time: atleast + random(0, interval) seconds
interval = 1800
atleast = 1800
browser = Browser('chrome', headless=False)

def login():
    browser.visit('https://quest.pecs.uwaterloo.ca/psp/SS/ACADEMIC/SA/?cmd=login&languageCd=ENG&')
    browser.find_link_by_text('Sign In').click()
    browser.find_by_id('username').fill(USERNAME)
    browser.find_by_id('password').fill(PASSWORD)
    browser.find_by_name('_eventId_proceed').click()


def to_enroll_page():
    browser.find_by_id('win0divPTNUI_LAND_REC_GROUPLET$2').click()
    sleep(3)
    with browser.get_iframe('main_target_win0') as fr:
        radio = fr.find_by_id('SSR_DUMMY_RECV1$sels$1$$0')
        radio.click()
        fr.find_by_id('DERIVED_SSS_SCT_SSR_PB_GO').click()


def try_enroll():
    sleep(3)
    with browser.get_iframe('main_target_win0') as fr:
        fr.find_by_text('Shopping Cart').click()
        fr.find_by_id('P_SELECT$1').click()
        fr.find_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL').click()
        fr.find_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT').click()
        text = fr.find_by_id('win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0').text
        if not text.startswith('Error:')
            print('Enroll result: {}'.format(text))
            exit(0)
        else:
            print('failed:', text[:20])


def logout():
    sleep(1)
    browser.find_by_id('PT_ACTION_MENU$PIMG').click()
    browser.find_link_by_text('Sign Out').click()


def main():
    while 1:
        print('start. now is {}'.format(datetime.now()))
        login()
        to_enroll_page()
        try_enroll()
        logout()
        slp = atleast + random.random() * interval
        print('finish. now is {}. sleep {}'.format(datetime.now(), slp))
        sleep(slp)


if __name__ == '__main__':
    main()
