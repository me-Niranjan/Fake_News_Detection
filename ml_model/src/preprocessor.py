"""
preprocessor.py - Text preprocessing utilities
"""
import re
import pandas as pd
from typing import List


class TextPreprocessor:
    """Handle text cleaning and preprocessing"""
    
    # Label mapping from 6 classes to 3 classes
    LABEL_MAPPING = {
        'true': 'REAL',
        'mostly-true': 'REAL',
        'half-true': 'NOT_ENOUGH_INFO',
        'barely-true': 'FAKE',
        'false': 'FAKE',
        'pants-fire': 'FAKE'
    }
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text
        
        Steps:
        - Remove URLs
        - Remove HTML tags
        - Remove email addresses
        - Remove special characters
        - Convert to lowercase
        - Remove extra whitespace
        
        Args:
            text: Input text to clean
        
        Returns:
            Cleaned text
        """
        if not isinstance(text, str):
            return ""
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters but keep apostrophes
        text = re.sub(r'[^a-zA-Z0-9\s\']', ' ', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    @staticmethod
    def convert_label(label: str) -> str:
        """
        Convert 6-class label to 3-class label
        
        Args:
            label: Original label from LIAR dataset
        
        Returns:
            Converted label (REAL, FAKE, NOT_ENOUGH_INFO)
        """
        return TextPreprocessor.LABEL_MAPPING.get(label, 'NOT_ENOUGH_INFO')
    
    @classmethod
    def preprocess_dataframe(cls, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply all preprocessing to dataframe
        
        Args:
            df: Input dataframe
        
        Returns:
            Preprocessed dataframe
        """
        df_processed = df.copy()
        
        # Convert labels
        df_processed['label'] = df_processed['label'].apply(cls.convert_label)
        
        # Clean text
        df_processed['claim'] = df_processed['claim'].apply(cls.clean_text)
        
        # Remove empty claims
        initial_len = len(df_processed)
        df_processed = df_processed[df_processed['claim'].str.len() > 0]
        removed = initial_len - len(df_processed)
        
        if removed > 0:
            print(f"⚠️  Removed {removed} rows with empty claims")
        
        return df_processed
    
    @staticmethod
    def get_text_statistics(texts: List[str]) -> dict:
        """
        Calculate text statistics
        
        Args:
            texts: List of text strings
        
        Returns:
            Dictionary with statistics
        """
        lengths = [len(t) for t in texts]
        word_counts = [len(t.split()) for t in texts]
        
        stats = {
            'avg_length': sum(lengths) / len(lengths),
            'max_length': max(lengths),
            'min_length': min(lengths),
            'avg_words': sum(word_counts) / len(word_counts),
            'max_words': max(word_counts),
            'min_words': min(word_counts)
        }
        return stats


if __name__ == "__main__":
    # Test preprocessing
    test_text = "Check this URL: http://example.com! It's <important> & should be cleaned."
    print("Original:", test_text)
    print("Cleaned: ", TextPreprocessor.clean_text(test_text))
    
    # Test label conversion
    print("\nLabel Mapping:")
    for old_label, new_label in TextPreprocessor.LABEL_MAPPING.items():
        print(f"  {old_label} → {new_label}")
