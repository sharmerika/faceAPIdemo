from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType

faceKey = "the_key_here"
endpoint = "the_endpoint_here"
credential = CognitiveServicesCredentials(faceKey)
face_client = FaceClient(endpoint, credential)

image_path = "image_path"

print("Opening image:", image_path)
print("Using endpoint:", endpoint)

with open(image_path, "rb") as image_stream:
    preview = image_stream.read(10)
    print("Image stream loaded:", preview)
    image_stream.seek(0)  # Reset stream before sending

    detected_faces = face_client.face.detect_with_stream(
        image=image_stream,
        detection_model='detection_03',
        recognition_model='recognition_04',
        return_face_id=False,
        return_face_attributes=[
            FaceAttributeType.age,
            FaceAttributeType.gender,
            FaceAttributeType.emotion
        ]
    )

    if not detected_faces:
        print("No face detected or invalid image.")
    else:
        print("Face detected.")
        for face in detected_faces:
            print("Age:", face.face_attributes.age)
            print("Gender:", face.face_attributes.gender)
            print("Emotions:", face.face_attributes.emotion)