from itertools import count
import requests
import re
import json
import urllib.parse
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
count=0
reset=0
st_count=0
def bar_custom(current, total,width=80):
    global count
    global reset
    
    # get percentage

    p=int(current/total*500)
    if(p<=0 and reset==0):
        print("Downding => ",end="")
        reset=reset+1
        
    
    if(p>count ):
        
        count=count+2
        print("*",end="")


    
def parse_str(string):
    global st_count
    st_count=st_count+1
    special_char = '@_!#$%^&*()<>?//\|}{~:;[]"'
    for i in special_char:
        try:
            
            string = string.replace(i, '')
            pattern = re.compile(r'\s+')
            string = re.sub(pattern, ' ', string)
        except:
            string = string.replace(i, '')
            pattern = re.compile(r'\s+')
            string = re.sub(pattern, ' ', string)
    
    return string



youtube_playlist_link = 'https://www.youtube.com/watch?v=7rDdXTe52_4&list=PLcT9BWAPAemXBW2AK2MBsWuP5_O2AJfeO'
f=urllib.parse.quote(youtube_playlist_link)

#url='https://youtubemultidownloader.org/scrapp/backend/yt-get.php?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dz9bZufPHFLU%26list%3DPLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ'
url='https://youtubemultidownloader.org/scrapp/backend/yt-get.php?url='+f


print(url)
x = requests.get(url)
res = json.loads(x.text)
res = res["items"]

count = 1
youtube_id=[]
video_string="https://www.youtube.com/watch?v="
file_name=[]
add_m=0

for i in res:
    #print(i["id"]," ",parse_str(i["title"]))

    youtube_id.append(video_string+str(i["id"]))
    #add_m=add_m+1
    file_name.append(str(parse_str(i["title"])))
    add_m=add_m+1
    
    
    count = count + 1



#print(youtube_id[0])



ik=0
counter_data=0



#   -----  >>>>>>>>>>>>>>>>>>>>>>>................................************


options=Options()
options.headless=True

options.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\him\\Desktop\\scrape_playlist\\c_neso"})
driver= webdriver.Chrome(executable_path="C:\\Users\\him\\Desktop\\chromedriver.exe",options=options)

while(ik<len(youtube_id)):
    try:
        counter_data=ik
        driver.get("https://en.savefrom.net/")    
        reset=0
        count=0
        
    
        driver.implicitly_wait(90)
        e=driver.find_element_by_css_selector("input[name='sf_url']").send_keys(youtube_id[ik])
        el = driver.find_elements_by_class_name("submit")
        
        for e in el:
            e.click()

        
        
        ed=driver.find_element_by_css_selector("div.def-btn-box > a")
    #ed=driver.find_element_by_css_selector("div.def-btn-box > a")
        val = ed.get_attribute("href")
        
        new_url=val
        f = open("demofile2.csv", "a")
        f.write(new_url)
        f.write(',')
        f.write('\n')
        f.close()
        #driver.get(url)
        driver.execute_script("window.open('');")  # commented section 
        
        driver.switch_to.window(driver.window_handles[1]) # commented section 
        #driver.get(new_url)
        
# Closing new_url tab
        #driver.close()
  
# Switching to old tab
        driver.switch_to.window(driver.window_handles[0])
    
        result=wget.download(val,file_name[ik]+".mp4",bar=bar_custom)
        
    
        
        
        ik=ik+1
        
    except:

        ik=counter_data
    
    print("value of Ik is :  ",ik)
    

    #nato -----------------00-0-0-0-0000-0000-00--
    


  
    

    
    

