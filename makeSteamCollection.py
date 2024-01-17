import os, sys, time
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fileName = "modpackFile.html"

htmlFile = open(R"Absolute_path_to_folder_where_modpackFile_is_located" + fileName, 'r', encoding="utf-8")
html = htmlFile.read()
soup = BeautifulSoup(html, features="lxml")
mods = []

title = soup.head.find("meta", {"name":"arma:PresetName"})

if title is None:
    title = soup.body.find('h1').find("strong")

    if title is None:
        title = fileName[:-5]
    else:
        title = title.text
else:
    title = title["content"]

modlist = soup.body.find('div', attrs={'class' : 'mod-list'}).findChildren("tr")
for mod in modlist:
    if(mod.find('span', attrs={'class' : 'from-steam'})):
        modLink = mod.find('a', attrs={'data-type' : 'Link'}).text
        mods.append(modLink.split('=')[-1])
    else:
        modName = mod.find('td', attrs={'data-type' : 'DisplayName'}).text
        print("The mod \"" + modName + "\" isn't loaded from steam, you'll need to add it manually to the server if it requires it")

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222") # Details in the repo README
service = Service(executable_path=R"Absolute_path_to_chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.switch_to.new_window('tab')
driver.get(R"https://steamcommunity.com/workshop/editcollection/?appid=107410")

assert "Workshop" in driver.title
elem = driver.find_element(By.ID, "title")
elem.clear()
elem.send_keys(title)

# Image for the preview, mandatory, square, at least 195px by 195px
upload_file = os.path.abspath(R"Absolute_path_to_image")
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)

driver.find_element(By.CSS_SELECTOR, R"#SubmitCollectionForm > div.editCollectionControls > a.btn_darkblue_white_innerfade.btn_medium.saveCollection").click()

driver.find_element(By.ID, R"MySubscribedItemsTab").click()

for mod in mods:
    try :
        driver.find_element(By.ID, R"choice_MySubscribedItems_" + mod).click()
    except:
        print("You're not subscribed to the modID " + mod + ", be sure to import the modpack in the arma launcher to subscribe to all of them\nYou need to finish this collection to delete it")
        sys.exit()


while (len(driver.find_elements(By.CSS_SELECTOR, R"#sortable_items > div")) != len(mods)):
    pass

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

hoverable = driver.find_element(By.CSS_SELECTOR, R"#editCollectionControls > a")
ActionChains(driver).move_to_element(hoverable).perform()

driver.find_element(By.CSS_SELECTOR, R"#editCollectionControls > a").click()
driver.find_element(By.CSS_SELECTOR, R"#BG_top_new_collection > div.newCollectionTabs > a").click()

while(len(driver.find_elements(By.CLASS_NAME, R"incompatibleNotification")) > 1):
    time.sleep(5)
    driver.refresh()

print(driver.current_url)


# Discord Webhook link if you want the final link to be posted in it, optional
link = R""

data = {
    "content" : driver.current_url
}

# Uncomment following line to post the collection link on discord
#result = requests.post(link, json = data)

# Uncomment following line to close the tab after the collection is published
#driver.close()
