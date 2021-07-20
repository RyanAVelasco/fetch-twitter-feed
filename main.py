from selenium import webdriver

## login information
url = r'https://twitter.com/'
username, password = (None, None)
## for selenium: logging in
homepage_login_button = 'div.r-13gxpu9 > span:nth-child(1) > span:nth-child(1)'
username_field = 'div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'
password_field = 'div.css-1dbjc4n:nth-child(7) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'
login_button = '.r-urgr8i' #twitter login pages
## logged in homepage
feed = 'div.r-1jgb5lz:nth-child(4)'
possible_tweeter_user = 'div.r-1jgb5lz:nth-child(4) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
containing_the_image = '#id__dct3gippevh > a:nth-child(1) > div:nth-child(1)'
containing_the_tweet = '#id__p7yvfo5fr6i > a:nth-child(1) > div:nth-child(1)'

## loading selenium
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

## login information
username = input('Please enter username: ').strip()
password = input('Please enter password: ').strip()

## main code starts here
with webdriver.Firefox(options=fireFoxOptions) as driver: # remove options=fireFoxOptions to show browser
    try:
        driver.get('https://twitter.com')
        print('twitter.com')

        ## login section below
        driver.find_element_by_css_selector(homepage_login_button).click()
        print('click login')
        driver.find_element_by_css_selector(username_field).send_keys(username)
        print('username')
        driver.find_element_by_css_selector(password_field).send_keys(password)
        print('password')
        driver.find_element_by_css_selector(login_button).click()
        print('click login')

    finally:
        input('press enter to exit')
        driver.quit()


