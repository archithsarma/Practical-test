from selenium import webdriver
search=input("Enter the file name")
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get('https://songsear.ch/')
sr='//*[@id="root"]/div/div/div[2]/div/form/div/div/input'
driver.find_element_by_xpath(sr).send_keys(search)
searchk='//*[@id="root"]/div/div/div[2]/div/form/div/div/span/button'
driver.find_element_by_xpath(searchk).click()
print("Since there can be multiple songs with the same name, select the correct one from the download link!! Download link is--------------")
print(driver.current_url)