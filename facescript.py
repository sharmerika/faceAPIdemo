from azure.identity import AzureCliCredential
from azure.keyvault.secrets import SecretClient
import requests
VAULT_URL = "vault_here"
credential = AzureCliCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)
FACE_API_KEY = client.get_secret("face_key").value
ENDPOINT = client.get_secret("faceEndpoint").value

IMAGE_PATH = "image_path"

url = ENDPOINT + "face/v1.0/detect"
params = {
    "returnFaceAttributes": "age, gender, emotion, smile",
    "returnFaceLandmarks": "false",
}
headers = {
    "Ocp-Apim-Subscription-Key": FACE_API_KEY,
    "Content-Type": "application/octet-stream"
}
with open(IMAGE_PATH, "rb") as img:
    response = requests.post(url, params=params, headers=headers, data=img)

for face in response.json():
    attrs = face["faceAttributes"]
    print(f"Age: {attrs['age']}, Gender: {attrs['gender']}")
    print("Emotions:")
    for emotion, score in attrs["emotion"].items():
        if score > 0.01:
            print(f" {emotion}: {round(score, 2)}")

def get_secret_value(secret_name, vault_url):
    credential = AzureCliCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value

VAULT_URL = "url_here"
FACE_API_KEY = get_secret_value("faceKey_primary", VAULT_URL)
ENDPOINT = get_secret_value("FaceAPI-Endpoint", VAULT_URL)

print(f"Key retrieved: {FACE_API_KEY[:5]} ... ")
print(f"Endpoint: {ENDPOINT}")

from azure.identity import AzureCliCredential
credential = AzureCliCredential()