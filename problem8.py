from selenium import webdriver
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf-FsUy0wzGdqpYCECZK5SNdGNMuY-dRGlLq96PlUkKoc3RHQ/viewform?embedded=true')
Fullname = '//*[@id="mG61Hd"]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
Email = '//*[@id="mG61Hd"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
Phone = '//*[@id="mG61Hd"]/div/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
Message= '//*[@id="mG61Hd"]/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[2]/textarea'
driver.find_element_by_xpath(Fullname).send_keys("Tony Stark")
driver.find_element_by_xpath(Email).send_keys("abc@xyz.com")
driver.find_element_by_xpath(Phone).send_keys("978272727")
driver.find_element_by_xpath(Message).send_keys("Hello")
