from selenium import webdriver
from lxml import html
from utils import utils, creds
from time import sleep
import random

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome(options=options)

def login():
    try:
        print('\nLogging In....\n')
        driver.get('https://mobile.facebook.com/login')
        sleep(4)
        driver.find_element_by_id('m_login_email').send_keys(creds.creds[0])
        driver.find_element_by_id('m_login_password').send_keys(creds.creds[1])
        driver.find_element_by_name('login').click()
        sleep(4)
        print('Logged in successfully.\n')
        return True
    except:
        print('\nLogin Failed....\n')  
        return False 

def run(profile_url):
    message_sent = False
    if 'profile.php?id' in profile_url:
        profile_id = profile_url.split('id=')[1].split('&')[0]
        driver.get(f'https://mobile.facebook.com/messages/thread/{profile_id}')
        sleep(2)
        try:
            send_message()
            message_sent = True
        except:
            utils.failed_log(profile_url)  
    else:
        profile_url = f'https://mobile.{profile_url.split("//")[1]}'
        driver.get(profile_url)
        sleep(2)
        try:
            driver.find_element_by_xpath("//a[contains(@href, 'messages/thread')]").click()
            sleep(2)
            send_message()
            message_sent = True
        except:
            utils.failed_log(profile_url)
    if message_sent is True:        
        print(f'Status => SENT\n')
    else:
        print(f'Status => FAILED\n')                     
    
def send_message():
    message_text = utils.message_to_send()
    driver.find_element_by_xpath("//textarea[@name='body'][1]").send_keys(message_text)
    sleep(1)
    driver.find_element_by_xpath("//input[@name='Send']").click()
    # driver.find_element_by_xpath("//textarea[@name='body'][1]").submit()

if __name__ == '__main__':
    login_staus = login()
    if login_staus:
        profile_urls = utils.read_profile_urls('profile_urls.txt')
        for profile_url in profile_urls:
            print(f'Sending Message => {profile_url}')
            run(profile_url)
            sleep(random.randint(4, 9))

    
