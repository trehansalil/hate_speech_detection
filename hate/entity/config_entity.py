from dataclasses import dataclass
from hate.constants import *
import os

@dataclass
class DataIngestionconfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_IMBALANCE_DATA_DIR)
        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)

@dataclass        
class DataValidationconfig:
    def __init__(self):        
        self.IMBALANCE_DATA_DIR = IMBALANCE_DATA_DIR
        self.RAW_DATA_DIR = RAW_DATA_DIR
        self.IMBALANCE_DATA_COLUMNS = IMBALANCE_DATA_COLUMNS
        self.RAW_DATA_COLUMNS = RAW_DATA_COLUMNS
        
@dataclass        
class DataTransformationconfig:
    def __init__(self):        
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_FILE_NAME)        
        self.ID = ID
        self.AXIS = AXIS   
        self.DROP_COLUMNS = DROP_COLUMNS
        self.CLASS = CLASS
        self.MAPPING_CLASS_COL_DICT = MAPPING_CLASS_COL_DICT   
        self.LABEL = LABEL    
        self.TWEET = TWEET    
        self.INPLACE = INPLACE              