import cv2
import numpy as np
import pickle
import imutils
import requests


#rectW,rectH=40,80
rectW,rectH=150,80
path_img = r'C:\Users\user\Desktop\GitHub\demo\Smart_City_Project\Car-Parking-Space-Counter-Detector-main\image.png'
try:
    with open('carParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+rectW and y1<y<y1+rectH:
                posList.pop(i)
    with open('carParkPos','wb') as f:
        pickle.dump(posList,f)
    
            
url = "http://192.168.1.3:8080/shot.jpg"
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    #
    # mg = imutils.resize(img, width=1000, height=1800)
    #img=cv2.imread(path_img)
    for pos in posList: cv2.rectangle(img,pos,(pos[0]+rectW,pos[1]+rectH),(0,0,255),2)
    
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)
