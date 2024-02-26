import os

from datetime import datetime


# common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'hatespeech2024'
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'label'
TWEET = 'tweet'


# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"


# Data validation constants
IMBALANCE_DATA_DIR = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_IMBALANCE_DATA_DIR)
RAW_DATA_DIR = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_DIR)
IMBALANCE_DATA_COLUMNS = ['id', 'label', 'tweet']
RAW_DATA_COLUMNS = ['Unnamed: 0', 'count', 'hate_speech', 'offensive_language',	'neither class', 'tweet']