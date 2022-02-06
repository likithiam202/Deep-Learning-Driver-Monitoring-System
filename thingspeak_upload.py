import urllib.request
import requests
import time


def upload_data(name,gps,off,image):
    try:
        URL='https://api.thingspeak.com/update?api_key=WB2WHZFU2S47FXL2'
        header='&field1={}&field2={}&field3={}&field4={}'.format(name,gps,off,image)
        new_url=URL+header
        data=urllib.request.urlopen(new_url)
        time.sleep(10)
        print(name,gps,off,image,"Uploaded")
    except:
        print("Failed to Upload")
  

name=["Jaffar","Karthik","SHIV","GAGAN"]
gps=["10N,21E","21S,22W","11N,41E","55S,32W"]
off=["Mobile","Turning_Back","Eyes_Closed","Mobile"]
image=["ff","gg","kk","mm"]
for i in range(0,4):
   upload_data(name[i],gps[i],off[i],image[i])


print("completed")    
