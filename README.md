# Arma3CollectionGenerator
This is a python script that will generate a steam collection using a modpack preset file on Chrome or Firefox

# Requirement
1. ```pip install -r requirements.txt```
2. Python 3.X (Tested on 3.9.16)
3. Download [Chromedriver.exe (for Chrome)](https://chromedriver.chromium.org/downloads) OR [Geckodriver.exe (for Firefox)](https://github.com/mozilla/geckodriver/releases)


# How to use for Firefox
1. Download the Firefox script somewhere on your computer
2. Download the geckodriver for your browser of choice and store it somewhere on your computer
3. Replace "Absolute_path_to_folder_where_modpackFile_is_located" on line 14 with the path to the folder contraining the modpack file (exemple : download folder)
4. Replace "Absolute_path_to_firefox" on line 41 with the path to firefox.exe
5. Replace "Absolute_path_to_geckodriver" on line 43 by the path to the geckodriver.exe
6. Replace "Absolute_path_to_image" on line 56 by the path to the image for your collection, has to be square shaped and at least 195x195 px
7. Before running the script :
    - You need to be sure you are logged in your steam account on firefox
    - If firefox was already running, you'll need to stop it completly (3 dot menu then "quit")
    - You need to be sure that you are subscribed to every mods listed in the html file, if one is missing the script will stop
    - You can simply drop the html in the arma launcher and it will subscribe to any missing mods
8. Run the python script, it should open a firefox window that is controlled by the script (it's recommended to close it after use), go to the steam page and generate a collection
9. At the end it will pause for 20-40 seconds and check for when steam finish analyzing the collection, it will then print the link of the collection, and if you want it can also send the link on discord via a webhook (see end of script).


# How to use for Chrome
1. Download the Chrome script somewhere on your computer
2. Download the geckodriver for your browser of choice and store it somewhere on your computer
3. Replace "Absolute_path_to_folder_where_modpackFile_is_located" on line 14 with the path to the folder contraining the modpack file (exemple : download folder)
4. Replace "Absolute_path_to_chrome" on line 41 with the path to chrome.exe
5. Replace "Absolute_path_to_chromedriver" on line 47 by the path to the chromedriver.exe
6. Replace "Absolute_path_to_image" on line 58 by the path to the image for your collection, has to be square shaped and at least 195x195 px
7. Before running the script :
    - You need to be sure you are logged in your steam account on chrome
    - If chrome was already running, you'll need to stop it completly (3 dot menu then "quit")
    - You need to be sure that you are subscribed to every mods listed in the html file, if one is missing the script will stop
    - You can simply drop the html in the arma launcher and it will subscribe to any missing mods
8. Run the python script, it should open a chrome window that is controlled by the script (it's recommended to close it after use), go to the steam page and generate a collection
9. At the end it will pause for 20-40 seconds and check for when steam finish analyzing the collection, it will then print the link of the collection, and if you want it can also send the link on discord via a webhook (see end of script).



There shouldn't be any issue but i know that my explanations can be very bad sometimes.
If there is any problem please open an issue and i'll try to help
