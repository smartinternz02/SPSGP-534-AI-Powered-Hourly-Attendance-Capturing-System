# Importing of Libraries
import boto3
import csv

client  = boto3.client('rekognition',\n",
                           aws_access_key_id = \"AKIA3S3TYBBZMYEBGUNI\",\n",
                           aws_secret_access_key = \"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\",\n",
                                                 region_name = 'us-east-2'\n",
                           )


# Defining a function to add faces to the collection
def add_faces_to_collection(bucket,photo,collection_id):
    
    #here, we have used MaxFaces as 1, so make sure you use only portrait images of the person
    #so that you can be sure which face has been detected and put into the collection.
    response = client.index_faces(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                ExternalImageId=photo,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
    
    
    print ('Results for ' + photo) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  External Id:' + faceRecord['Face']["ExternalImageId"])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
    
         
    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return len(response['FaceRecords'])

# Defining a main function 
def main():
    bucket = 'students123'  #Your Bucket Name 
    collection_id='students'  #Your Collection Name you created in the last step   
    #List the names of all the photos you want to put in the colletion
    #these are the filepaths of the images in AWS S3
    # give them names in such a way that removing the last 4 characters of filename,which will be 
    # ".jpg", we can get to know the name of person and thus create folders by that name further.
    photos = ["sehwag.jpg","Ganguly.jpg","kapildev.jpg"]
    
    for photo in photos:
        indexed_faces_count=add_faces_to_collection(bucket, photo, collection_id)
        print("Faces indexed count: " + str(indexed_faces_count))
    
    
if __name__ == "__main__":
    main()







