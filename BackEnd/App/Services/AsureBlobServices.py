
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
 
# Charge automatiquement les variables du fichier .env (à la racine du projet)
load_dotenv()
 
# --- Configuration -----------------------------------------------------------
# Les valeurs sont lues depuis le fichier .env (voir .env.example)
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "")

#Connect to container
def _connect_to_container():
    try:
        blob_service_st = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_st.get_container_client(CONTAINER_NAME)
        return container_client
    except Exception as e:
        raise ValueError(f"Erreur lors de la connexion au conteneur Azure Blob Storage: {e}")

def azureBlobUpload(file):
    try:
        container_client = _connect_to_container()
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file.file, overwrite=True)
        url_file=blob_client.url
    except Exception as e:
        raise ValueError(f"Erreur lors de l'upload du fichier: {e}")

    return url_file

def azureBlobGet():
    try:
        container_client = _connect_to_container()
        blobs_list = container_client.list_blobs()
        urls = [container_client.get_blob_client(blob.name).url for blob in blobs_list]
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération des fichiers: {e}")

    return urls