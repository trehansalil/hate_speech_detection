import inspect
import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.components.data_ingestion import DataIngestion
from hate.components.data_validation import DataValidation
from hate.components.data_transformation import DataTransformation
from hate.entity.config_entity import DataIngestionconfig, DataValidationconfig, DataTransformationconfig
from hate.entity.artifact_entity import DataIngestionArtifacts, DataValidationArtifacts, DataTransformationArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionconfig()
        self.data_validation_config = DataValidationconfig()
        self.data_transformation_config = DataTransformationconfig()
        
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
    
    def start_data_validation(self) -> DataValidationArtifacts:
        current_function_name = inspect.stack()[0][3]
        try:
            logging.info(f"Starting Validation of data using the {current_function_name} method of {self.__class__.__name__} class")
            data_validation = DataValidation(data_validation_config = self.data_validation_config)
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info(f"Data Validated using the {current_function_name} method of {self.__class__.__name__} class")
            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e       
        
    def start_data_transformation(self, data_ingestion_artifacts: DataIngestionArtifacts, data_validation_artifacts: DataValidationArtifacts) -> DataTransformationArtifacts:
        current_function_name = inspect.stack()[0][3]
        try:
            logging.info(f"Starting Transformation of data using the {current_function_name} method of {self.__class__.__name__} class")
            
            data_transformation = DataTransformation(
                data_transformation_config = self.data_transformation_config, 
                data_ingestion_artifacts = data_ingestion_artifacts, 
                data_validation_artifacts = data_validation_artifacts                
            )
            
            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            logging.info(f"Data Transformation using the {current_function_name} method of {self.__class__.__name__} class")
            return data_transformation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e             
             
    def run_pipeline(self):
        current_function_name = inspect.stack()[0][3]
        logging.info(f"Started the {current_function_name} method of {self.__class__.__name__} class")
        
        try:
            logging.info(f"Starting Ingestion using the {current_function_name} method of {self.__class__.__name__} class")
            data_ingestion_artifacts = self.start_data_ingestion()

            logging.info(f"Starting Validation using the {current_function_name} method of {self.__class__.__name__} class")            
            data_validation_artifacts = self.start_data_validation()
 
            logging.info(f"Starting Transformation using the {current_function_name} method of {self.__class__.__name__} class")            
            data_validation_artifacts = self.start_data_transformation(data_ingestion_artifacts=data_ingestion_artifacts, 
                                                                   data_validation_artifacts=data_validation_artifacts)           
            logging.info(f"Exited the {current_function_name} method of {self.__class__.__name__} class")
        except Exception as e:
            raise CustomException(e, sys) from e           