"""
Data loading and preprocessing utilities for the Air Passenger Satisfaction application.
This module provides functions to load and preprocess airline data.
"""
import pickle
import pandas as pd
from typing import Tuple
from src.config.constants import (
    DATA_FILE_PATH,
    CLASS_MAPPINGS,
    SATISFACTION_MAPPINGS,
    GENDER_MAPPINGS,
    CUSTOMER_TYPE_MAPPINGS,
    TRAVEL_TYPE_MAPPINGS,
    COL_SATISFACTION,
    COL_GENDER,
    COL_CUSTOMER_TYPE,
    COL_TRAVEL_TYPE,
    COL_CLASS
)


def load_airline_data() -> pd.DataFrame:
    """
    Load airline data from pickle file.
    
    Returns:
        pd.DataFrame: Raw airline data
    
    Raises:
        FileNotFoundError: If the data file is not found
        Exception: If there's an error loading the data
    """
    try:
        with open(DATA_FILE_PATH, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found at: {DATA_FILE_PATH}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


def preprocess_airline_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess airline data by replacing numeric codes with descriptive labels.
    
    Args:
        data: Raw airline data DataFrame
        
    Returns:
        pd.DataFrame: Preprocessed airline data with descriptive labels
    """
    # Create a copy to avoid modifying the original data
    processed_data = data.copy()
    
    # Replace class codes with labels
    processed_data.iloc[:, COL_CLASS] = processed_data.iloc[:, COL_CLASS].replace(CLASS_MAPPINGS)
    
    # Replace satisfaction codes with labels
    processed_data.iloc[:, COL_SATISFACTION] = processed_data.iloc[:, COL_SATISFACTION].replace(SATISFACTION_MAPPINGS)
    
    # Replace gender codes with labels
    processed_data.iloc[:, COL_GENDER] = processed_data.iloc[:, COL_GENDER].replace(GENDER_MAPPINGS)
    
    # Replace customer type codes with labels
    processed_data.iloc[:, COL_CUSTOMER_TYPE] = processed_data.iloc[:, COL_CUSTOMER_TYPE].replace(CUSTOMER_TYPE_MAPPINGS)
    
    # Replace travel type codes with labels
    processed_data.iloc[:, COL_TRAVEL_TYPE] = processed_data.iloc[:, COL_TRAVEL_TYPE].replace(TRAVEL_TYPE_MAPPINGS)
    
    return processed_data


def get_processed_airline_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load and preprocess airline data.
    
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing:
            - processed_data: Preprocessed data with descriptive labels
            - raw_data: Original raw data with numeric codes
    """
    raw_data = load_airline_data()
    processed_data = preprocess_airline_data(raw_data)
    
    return processed_data, raw_data


def aggregate_satisfaction_by_class(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate satisfaction counts by class.
    
    Args:
        data: Preprocessed airline data
        
    Returns:
        pd.DataFrame: Aggregated data with satisfaction counts per class
    """
    return data.groupby(['satisfaction', 'Class'], as_index=False)[['Online boarding']].count()


def aggregate_satisfaction_by_customer_type(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate satisfaction counts by customer type and class.
    
    Args:
        data: Preprocessed airline data
        
    Returns:
        pd.DataFrame: Aggregated data with satisfaction counts per customer type and class
    """
    return data.groupby(['satisfaction', 'Customer Type', 'Class'], as_index=False)[['Online boarding']].count()


def aggregate_satisfaction_by_gender(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate satisfaction counts by gender and class.
    
    Args:
        data: Preprocessed airline data
        
    Returns:
        pd.DataFrame: Aggregated data with satisfaction counts per gender and class
    """
    return data.groupby(['satisfaction', 'Gender', 'Class'], as_index=False)[['Online boarding']].count()


def aggregate_satisfaction_by_travel_type(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate satisfaction counts by travel type and class.
    
    Args:
        data: Preprocessed airline data
        
    Returns:
        pd.DataFrame: Aggregated data with satisfaction counts per travel type and class
    """
    return data.groupby(['satisfaction', 'Type of Travel', 'Class'], as_index=False)[['Online boarding']].count()


def aggregate_ratings_by_category(data: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Aggregate ratings counts by a specific category.
    
    Args:
        data: Preprocessed airline data
        category: The category column name to aggregate by
        
    Returns:
        pd.DataFrame: Aggregated data with counts per category rating
    """
    return data.groupby([category], as_index=False)[['Online boarding']].count()
