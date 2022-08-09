import cv
import random
import time
import dropbox
start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img"+ str(number)+".png"
        
        cv2.imwrite(image_name, frame)  
        start_time = time.time
        result = False
    return image_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "sl.BL5WyjrVSJEM8mR5eCDL2QSLrFKR505izAAot-0p0kOm7Lc447m5l4ExFJMlBIA9n9sm8_0R7O1--3w9ovpM3UMmPlGqefu4yIt7r2E1m7La6N1ZIC2JZOZv3iICVxaROE5jU-4"
    file = image_name
    file_from = file
    file_to = "/newfolder1"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb')as f:
         dbx.file_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
         print("file_uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)   

main() 
