from selenium import webdriver
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.maximize_window()
Username = '//*[@id="identifierId"]'
driver.find_element_by_xpath(Username).send_keys("username")
Next = '//*[@id="identifierNext"]/span/span'
driver.find_element_by_xpath(Next).click()
Password = '//*[@id="password"]/div[1]/div/div[1]/input'
driver.find_element_by_xpath(Password).send_keys("Password")
Next1= '//*[@id="passwordNext"]/div[2]'
driver.find_element_by_xpath(Next1).click()
search='//*[@id="gs_lc50"]/input[1]'
driver.find_element_by_xpath(search).send_keys("congratulations")
sk='//*[@id="aso_search_form_anchor"]/button[4]/svg/path[1]'
driver.find_element_by_xpath(sk).click()



