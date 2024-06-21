import os
from google.cloud import storage

def download_model():
    client = storage.Client()
    bucket = client.bucket(os.getenv('CLOUD_STORAGE_BUCKET'))
    blob = bucket.blob(os.getenv('MODEL_PATH'))
    model_local_path = 'model.pkl'
    blob.download_to_filename(model_local_path)
    return model_local_path

