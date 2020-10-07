import datetime
import json
from selenium import webdriver
import time

eleNM = None

def wish_birth(name):
    return "Happy Birthday" + name.split(" ")[0] + "!!"

def getJsonData(file, attr_ret, attr1, attr2, attr_val1, attr_val2):
    data = json.load(file)
    retv = []
    for i in data :
        if(i[attr1] == attr_val1 and i[attr2] == attr_val2):
            retv.append(i[attr_ret])
    return retv

data_file = open("config.json", "r")
namev = []
print("Script Running")

while True:
    try:
        datt = datetime.datetime.now()
        namev = getJsonData(data_file, "name", "birth_month", "birth_date", str(datt.month), str(datt.day))

    except json.decoder.JSONDecodeError:
        continue
    if(namev != []):
        break

##chropt = webdriver.ChromeOptions()
##chropt.add_argument("")    
driver = webdriver.Chrome(executable_path = r"C:\Users\DEEPSHIKHA\Downloads\chromedriver_win32")  
driver.get("https://web.whatsapp.com/") 

time.sleep(10)

print(namev)

for inp in namev:
    try:
        eleNM = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]'.format(inp))
    except Exception as ex:
        print(ex)
        continue
    eleNM.click() 

    while(True):
        eleTF = driver.find_element_by_class_name("_13mgZ")
        eleTF.send_keys(wish_birth(inp))
        eleSND = driver.find_element_by_class_name("_3M-N-") 
        eleSND.click() 
        break