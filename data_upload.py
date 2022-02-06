from mega import Mega
import urllib.request
import requests
import time

mega=Mega()
m=mega.login("p1projectteam66@gmail.com","Actual_Password")

def img_2_link(file_name):
    folder=m.find('Dri1')  #finds the drivers folder
    img=m.upload(file_name,folder[0]) #uploads image to the above folder
    link=m.get_upload_link(img) #returns link
    da=""
    for i in range(21,len(link)):
        da+=str(link[i])
    return da 

def upload_data(name,gps,off,image):
    try:
        URL='https://api.thingspeak.com/update?api_key=WB2WHZFU2S47FXL2' #channels url with key
        header='&field1={}&field2={}&field3={}&field4={}'.format(name,gps,off,image) #adding data of required fields
        new_url=URL+header
        data=urllib.request.urlopen(new_url)
        time.sleep(15)
        print(name,gps,off,image,"Uploaded") 
    except:
        print("Failed to Upload")

#sample data to be uploaded
name=["Jaffar","Karthik","Shiv","Gagan","Kevin","Goutham"]
gps=["10N,21E","21S,22W","11N,41E","55S,32W","22N,31E","54N,33E"]
off=["Mobile","Turning_Back","Eyes_Closed","Mobile","Mobile","Turning_Back"]
file_name=['img_229.jpg','img_230.jpg','img_234.jpg','img_235.jpg','img_236.jpg','img_237.jpg']

for i in range(0,len(off)):
    image_link=img_2_link(file_name[i])
    upload_data(name[i],gps[i],off[i],image_link)

print("completed")
