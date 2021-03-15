# Importing of Libraries
import boto3
import csv

# Creation of Client
client  = boto3.client('rekognition',\n",
                           aws_access_key_id = \"AKIA3S3TYBBZMYEBGUNI\",\n",
                           aws_secret_access_key = \"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\",\n",
                                                 region_name = 'us-east-2'\n",
                           )

# Defining function to list the faces
def list_faces_in_collection(collection_id):

    maxResults=2
    faces_count=0
    tokens=True
   #using built in function of rekognition
    response=client.list_faces(CollectionId=collection_id,
                               MaxResults=maxResults)

    print('Faces in collection : ' + collection_id

    while tokens:
        faces=response['Faces']
        #to print details of each face in the collection
        for face in faces:
            print("Face Id     : " + face["FaceId"]) #The id by which Rekognition knows this face
            print("External Id : " + face["ExternalImageId"]) #The name by which we know the face.
            faces_count+=1
            
        if 'NextToken' in response:
            nextToken=response['NextToken']
            response=client.list_faces(CollectionId=collection_id,
                                       NextToken=nextToken,MaxResults=maxResults)
        else:
            tokens=False
    return faces_count #returns the total number of faces found in collection

def main():
    bucket = 'students123' # Replace with your bucket name
    collection_id='students' # Replace with your collection id
    
    faces_count=list_faces_in_collection(collection_id)
    print("faces count: " + str(faces_count))

if __name__ == "__main__":
    main()

