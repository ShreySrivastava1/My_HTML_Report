from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random, time, sys, traceback, pytest


driver = webdriver.Chrome(executable_path='/home/shrey/Downloads/chromedriver-linux64/chromedriver')
wait = WebDriverWait(driver, 20)

driver.maximize_window()
main_window = driver.current_window_handle

driver.get('https://nextinstance-dot-react-staging.de.r.appspot.com/')
# driver.get('https://www.thesqua.re/')
time.sleep(3)

def test_currency_tab():

    currency_set_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header > div.css-fcjucu > div > div > div > div > div.header-right > div.header-curr-menu > div > div > div')))
    currency_set_btn.click()

    currency_choose = driver.find_element(By.CSS_SELECTOR, '#menu-currency > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.MuiMenu-paper.MuiMenu-paper.css-adx198')

    for _ in range(random.randrange(2,10)):
        currency_choose.send_keys(Keys.DOWN)
    currency_choose.click()

    time.sleep(2)


def test_search_bar():

    # l = random.choice(['london','paris',"new york",'amsterdam','singapore','dubai','tokyo',"san francisco",'dublin',"Hong Kong",'berlin','sydney'])

    # l = 'london'
    # search_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > main > div > div.hero-banner.css-1k0v9lv > div.MuiContainer-root.MuiContainer-maxWidthLg.container.css-1qsxih2 > div.desktop-only-768 > div > div > div:nth-child(1) > div > div > div > div > button')))
    # search_bar.click()

    # search_input_field = driver.find_element(By.CSS_SELECTOR, '#__next > main > div > div.hero-banner.css-1k0v9lv > div.MuiContainer-root.MuiContainer-maxWidthLg.container.css-1qsxih2 > div.desktop-only-768 > div > div > div:nth-child(1) > div > div > div')
    # input_field = search_input_field.find_element(By.ID, 'desktop-search-bar')
    # input_field.send_keys(l)

    # time.sleep(4)
    # for _ in range(random.randrange(2,10)):
    #     input_field.send_keys(Keys.DOWN)
    # input_field.send_keys(Keys.ENTER)

    dropdown_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '*.header-dest-menu .header-menu-link')))
    dropdown_menu.click()

    city_choice = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '*.about_link_style')))
    city_choice.click()

    service_apt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header > div.css-fcjucu > div > div > div > div > div.header-right > div.header-menu-sec > ul > li.header-dest-menu > ul > li:nth-child(1) > ul > div > div:nth-child(5) > a')))
    service_apt.click()

    time.sleep(2)


all_windows = driver.window_handles
new_window = all_windows[-1]
driver.switch_to.window(new_window)

def test_filter():
    
    filter_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > main > div:nth-child(10) > div > div:nth-child(3) > div > a:nth-child(3)')))

    driver.execute_script("arguments[0].click();", filter_menu)

    # import pdb; pdb.set_trace()

    element = driver.find_element(By.CSS_SELECTOR, '#canary-gateway-apartments-226097697 > div > div:nth-child(2) > a > div > div.block__elem--property--right.mr-10 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-3nargb > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-5.css-8e4lkk > div > p')

    # loc = element.location
    size = element.size

    assert (size.get('width') == 129.09) and (size.get('height') == 15), "Text size for 'Nights Min stay' differ: original {'height': 15, 'width': 139} where as after change {'height': 15, 'width': 102}"