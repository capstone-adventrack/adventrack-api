import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    CLOUD_STORAGE_BUCKET = os.getenv('CLOUD_STORAGE_BUCKET')
    MODEL_PATH = os.getenv('MODEL_PATH')
    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')
