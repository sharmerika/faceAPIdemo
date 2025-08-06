import os
import csv
from azure.identity import AzureCliCredential
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials

credential = AzureCliCredential()

endpoint = "the_endpoint_here"
face_client = FaceClient(endpoint, credential)

csv_path = 'fac_output.csv'
csv_file = open(csv_path, 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['Filename', 'Age', 'Gender', 'Emotion'])

folder_path = r"your_path_here"


for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(folder_path, filename)
        print(f"\nProcessing: {filename}")
        with open(image_path, "rb") as image_stream:
            detected_faces = face_client.face.detect_with_stream(
                image=image_stream,
                detection_model='detection_03',
                return_face_attributes=[FaceAttributeType.age, FaceAttributeType.gender, FaceAttributeType.emotion
                ]
            )
            for face in detected_faces:
                age = face.face_attributes.age
                gender = face.face_attributes.gender
                emotion = face.face_attributes.emotion
                dominant_emotion = max(face.face_attributes.emotion.items(), key=lambda item: item[1])[0]
                print(f" - Age: {face.face_attributes.age}")
                print(f" - Gender: {face.face_attributes.gender}")
                print(f" - Emotion: {face.face_attributes.emotion}")
                writer.writerow([filename, age, gender, emotion])

csv_file.close()
print(f"\nResults saved to {csv_path}")