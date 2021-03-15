# Importing of Libraries
import boto3
import csv

# Create client 
client  = boto3.client('rekognition',\n",
                           aws_access_key_id = \"AKIA3S3TYBBZMYEBGUNI\",\n",
                           aws_secret_access_key = \"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\",\n",
                                                 region_name = 'us-east-2'\n",
                           )
def create_collection(collection_id): 

    #Create a collection
    print('Creating collection:' + collection_id)
    
    #Using inbuilt function within rekognition client
    response=client.create_collection(CollectionId=collection_id) 
    
    #Printing the collection details, save the printed output in a text file.
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='students' #Assign Collection ID Name
    create_collection(collection_id) # Creation of Collection ID

if __name__ == "__main__":
    main() 
    
    