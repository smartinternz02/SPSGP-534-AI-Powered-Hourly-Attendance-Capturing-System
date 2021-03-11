# Importing of Liraries
import cv2
import boto3
import csv
import datetime as dt
import time
import imutils
import requests

# Enabling the Cv2 
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # xml file to detect the faces 

# Creation of client to rekognition Service
client  = boto3.client('rekognition',
                       aws_access_key_id = "AKIA2QI47CMUMJL6LW6D",
                       aws_secret_access_key = "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",
                                             region_name = 'us-east-2')
# Creation of client to S3 Service
s3client  = boto3.client('s3',
                       aws_access_key_id = "AKIA2QI47CMUMJL6LW6D",
                       aws_secret_access_key = "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",
                                             region_name = 'us-east-1'
                       )

# Declaring global Variables 
global name,period,url
    
# Defining of upload image function to S3         
def uploadimage():
    
    bucket = 'students123' # Replace with your bucket name
    
    filename = 'test.jpg' # Naming of captured to store in S3
    relative_filename = 'test.jpg' 
    
    s3client.upload_file(filename, bucket, relative_filename)
    print("file Uploaded")
                     
# Comparing of the captures image with S3
def photo():
    
    bucket = 'students123' # Replace with your bucket name
    collection_id = 'students'
    fileNames = ['test.jpg']
    threshold = 70 # Threshold limit for the similarity
    maxFaces = 2
    #here max faces is the number of faces it shoudl give as output if more than 1 face is
    #being rekognized with abover threshold confidence,
    for fileName in fileNames:
        response=client.search_faces_by_image(CollectionId=collection_id,
                                    Image={'S3Object':
                                           {'Bucket':bucket,
                                            'Name':fileName}},
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
    
        faceMatches=response['FaceMatches']
        print ('Matching faces')
        for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('External Id:' + match['Face']["ExternalImageId"])
            #Assigning a variable for external id
            name1=match['Face']["ExternalImageId"]
            name=name1.split(".") # Spliting the External id to remove .jpg extension
            name=name[0]
            date=str(dt.datetime.now())[0:11] # Capturing time
            time=time_1.strftime('%H')
            period = ""
            if(time == '9'):
                period = "Period1"
            elif(time == '10'):
                period = "Period2"
            else:
                period = "Period3"
            # Hitting API Gateway url to send captured image name & period
            url = "https://70htd9zo98.execute-api.us-east-2.amazonaws.com/attendance_input?name="+name+"&period="+period
            status = requests.request("GET",url)
            print(status.json())
            print("uploaded to DB")
            print("Student Detected :"+name)
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
       
        
# Main function         
while True:
    
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    time_1 = dt.datetime.now()
    print("present time:",time_1)
    hr = time_1.strftime('%H')
    sd = time_1.minute;
    
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
            scaleFactor=1.2,
            minNeighbors=5
           # minSize=(30, 30)
        )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        print (faces.shape)
        cv2.putText(frame, "faces detected: " + str(faces.shape[0]), (50, 30),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w+30, y+h+30), (0, 255, 0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h+30, x:x+w+30]
        imgname = "test.jpg"
        cv2.imwrite(imgname, roi_color)
        uploadimage()
        a =  photo()
        print(a)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    cv2.imshow('Video', frame)
    
    
video_capture.release()
cv2.destroyAllWindows()
    
    


