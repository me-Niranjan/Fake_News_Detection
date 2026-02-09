"""
utils.py - Utility functions
"""
import os
import json
import pickle
import numpy as np
import pandas as pd
from typing import Any, Dict


class FileManager:
    """Manage file I/O operations"""
    
    @staticmethod
    def create_dir(path: str):
        """Create directory if it doesn't exist"""
        os.makedirs(path, exist_ok=True)
    
    @staticmethod
    def save_json(data: Dict, filepath: str):
        """Save dictionary as JSON"""
        FileManager.create_dir(os.path.dirname(filepath))
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Saved: {filepath}")
    
    @staticmethod
    def load_json(filepath: str) -> Dict:
        """Load JSON file"""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def save_pickle(data: Any, filepath: str):
        """Save object as pickle"""
        FileManager.create_dir(os.path.dirname(filepath))
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        print(f"✅ Saved: {filepath}")
    
    @staticmethod
    def load_pickle(filepath: str) -> Any:
        """Load pickle file"""
        with open(filepath, 'rb') as f:
            return pickle.load(f)


class MetricsCalculator:
    """Calculate evaluation metrics"""
    
    @staticmethod
    def calculate_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate accuracy"""
        return np.mean(y_true == y_pred)
    
    @staticmethod
    def calculate_precision(y_true: np.ndarray, y_pred: np.ndarray, label: int = 1) -> float:
        """Calculate precision for specific label"""
        true_positives = np.sum((y_pred == label) & (y_true == label))
        predicted_positives = np.sum(y_pred == label)
        
        if predicted_positives == 0:
            return 0.0
        
        return true_positives / predicted_positives
    
    @staticmethod
    def calculate_recall(y_true: np.ndarray, y_pred: np.ndarray, label: int = 1) -> float:
        """Calculate recall for specific label"""
        true_positives = np.sum((y_pred == label) & (y_true == label))
        actual_positives = np.sum(y_true == label)
        
        if actual_positives == 0:
            return 0.0
        
        return true_positives / actual_positives
    
    @staticmethod
    def calculate_f1(precision: float, recall: float) -> float:
        """Calculate F1 score"""
        if precision + recall == 0:
            return 0.0
        
        return 2 * (precision * recall) / (precision + recall)


class DataProcessor:
    """Process and transform data"""
    
    @staticmethod
    def balance_dataset(df: pd.DataFrame, label_col: str = 'label', 
                       sampling: str = 'undersample') -> pd.DataFrame:
        """
        Balance dataset
        
        Args:
            df: DataFrame
            label_col: Label column name
            sampling: 'oversample' or 'undersample'
        
        Returns:
            Balanced dataframe
        """
        label_counts = df[label_col].value_counts()
        
        if sampling == 'undersample':
            min_count = label_counts.min()
            balanced_dfs = []
            
            for label in df[label_col].unique():
                label_df = df[df[label_col] == label]
                balanced_dfs.append(label_df.sample(n=min_count, random_state=42))
            
            return pd.concat(balanced_dfs, ignore_index=True)
        
        return df
    
    @staticmethod
    def train_val_test_split(df: pd.DataFrame, train_size: float = 0.7, 
                            val_size: float = 0.15, random_state: int = 42):
        """
        Split data into train, val, test
        
        Args:
            df: DataFrame
            train_size: Proportion for training
            val_size: Proportion for validation
            random_state: Random seed
        
        Returns:
            Tuple of (train_df, val_df, test_df)
        """
        df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
        
        train_idx = int(len(df) * train_size)
        val_idx = int(len(df) * (train_size + val_size))
        
        train = df[:train_idx]
        val = df[train_idx:val_idx]
        test = df[val_idx:]
        
        return train, val, test


if __name__ == "__main__":
    # Test utilities
    print("✅ Utility functions loaded successfully")
