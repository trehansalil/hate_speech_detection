from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str

@dataclass    
class DataValidationArtifacts:    
    imbalance_data_valid: bool
    raw_data_valid: bool