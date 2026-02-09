"""
data_loader.py - Load and manage datasets
"""
import pandas as pd
import os
from typing import Tuple


class DataLoader:
    """Load and manage LIAR dataset"""
    
    def __init__(self, data_path: str = './preprocessed_data'):
        """
        Initialize DataLoader
        
        Args:
            data_path: Path to preprocessed data directory
        """
        self.data_path = data_path
        self.train_df = None
        self.test_df = None
        self.val_df = None
        self.combined_df = None
    
    def load_preprocessed_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Load preprocessed train, test, val datasets
        
        Returns:
            Tuple of (train_df, test_df, val_df)
        """
        self.train_df = pd.read_csv(os.path.join(self.data_path, 'train_data.csv'))
        self.test_df = pd.read_csv(os.path.join(self.data_path, 'test_data.csv'))
        self.val_df = pd.read_csv(os.path.join(self.data_path, 'val_data.csv'))
        
        print(f"✅ Train set: {self.train_df.shape}")
        print(f"✅ Test set: {self.test_df.shape}")
        print(f"✅ Val set: {self.val_df.shape}")
        
        return self.train_df, self.test_df, self.val_df
    
    def load_combined_data(self) -> pd.DataFrame:
        """
        Load combined dataset
        
        Returns:
            Combined dataframe
        """
        self.combined_df = pd.read_csv(os.path.join(self.data_path, 'combined_data.csv'))
        print(f"✅ Combined dataset: {self.combined_df.shape}")
        return self.combined_df
    
    def get_claims_by_label(self, df: pd.DataFrame, label: str):
        """
        Get all claims for a specific label
        
        Args:
            df: DataFrame
            label: Label to filter by (REAL, FAKE, NOT_ENOUGH_INFO)
        
        Returns:
            Filtered dataframe
        """
        return df[df['label'] == label]
    
    def get_statistics(self, df: pd.DataFrame) -> dict:
        """
        Get dataset statistics
        
        Args:
            df: DataFrame
        
        Returns:
            Dictionary with statistics
        """
        stats = {
            'total_samples': len(df),
            'unique_speakers': df['speaker'].nunique(),
            'label_distribution': df['label'].value_counts().to_dict(),
            'avg_claim_length': df['claim'].str.len().mean(),
            'missing_values': df.isnull().sum().to_dict()
        }
        return stats


if __name__ == "__main__":
    loader = DataLoader()
    train, test, val = loader.load_preprocessed_data()
    print("\nStatistics:")
    print(loader.get_statistics(train))
