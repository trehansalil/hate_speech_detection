import inspect
import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.components.data_ingestion import DataIngestion
from hate.entity.config_entity import DataIngestionconfig
from hate.entity.artifact_entity import DataIngestionArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionconfig()
        
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        current_function_name = inspect.stack()[0][3]
        try:
            logging.info(f"Getting the data from GCloud Storage bucket using the {current_function_name} method of {self.__class__.__name__} class")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info(f"Got the train and validation data from GCloud Storage using the {current_function_name} method of {self.__class__.__name__} class")
            logging.info(f"Exited the {current_function_name} method of {self.__class__.__name__} class")
            
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e   
             
    def run_pipeline(self):
        current_function_name = inspect.stack()[0][3]
        logging.info(f"Started the {current_function_name} method of {self.__class__.__name__} class")
        
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            logging.info(f"Exited the {current_function_name} method of {self.__class__.__name__} class")
            
        except Exception as e:
            raise CustomException(e, sys) from e           