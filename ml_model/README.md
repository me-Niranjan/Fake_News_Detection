# Fake News Detection - ML Module

## Project Overview
This is the **ML component** of the Fake News Detection system. It handles:
- Data acquisition from LIAR dataset
- Text preprocessing and cleaning
- Feature extraction & embedding generation
- Training semantic similarity model
- Training NLI (Natural Language Inference) model
- Model evaluation and validation

## 📁 Project Structure

```
ml_model/
├── notebooks/                      # Jupyter notebooks for experimentation
│   ├── 01_data_exploration.ipynb        # LIAR dataset EDA
│   ├── 02_data_preprocessing.ipynb      # Text cleaning & label conversion
│   ├── 03_feature_extraction.ipynb      # Feature engineering
│   ├── 04_semantic_similarity_model.ipynb
│   ├── 05_nli_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_full_pipeline_testing.ipynb
│
├── src/                            # Reusable Python modules
│   ├── data_loader.py              # Load datasets
│   ├── preprocessor.py             # Text preprocessing
│   ├── utils.py                    # Utility functions
│   ├── semantic_similarity.py       # Semantic model
│   ├── nli_model.py                # NLI model
│   ├── evidence_retriever.py        # Evidence retrieval
│   └── claim_verifier.py            # Main pipeline
│
├── data/                           # Raw datasets (from Kaggle)
│   ├── train.tsv
│   ├── test.tsv
│   └── val.tsv
│
├── preprocessed_data/              # Cleaned & processed data
│   ├── train_data.csv
│   ├── test_data.csv
│   ├── val_data.csv
│   └── combined_data.csv
│
├── models/                         # Saved trained models
│   ├── tokenizer.pkl
│   ├── semantic_model.pth
│   ├── nli_model.pth
│   └── embeddings.npy
│
├── configs/                        # Configuration files
│   ├── model_config.json
│   ├── paths_config.json
│   └── training_config.yaml
│
├── outputs/                        # Results & metrics
│   ├── metrics.json
│   ├── training_logs.txt
│   ├── predictions.json
│   └── confusion_matrix.png
│
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download LIAR Dataset (for Colab)
- Go to https://www.kaggle.com/
- Download LIAR dataset: https://www.kaggle.com/datasets/liar-dataset/liar-plus
- Extract to `data/` folder

### 3. Run Notebooks in Order
1. **Notebook 01**: Data Exploration
2. **Notebook 02**: Data Preprocessing
3. **Notebook 03**: Feature Extraction
4. **Notebook 04**: Semantic Similarity Model
5. **Notebook 05**: NLI Model Training
6. **Notebook 06**: Model Evaluation
7. **Notebook 07**: Full Pipeline Testing

## 📊 Dataset Information

**LIAR Dataset:**
- **Size**: ~12,836 claims
- **Labels**: 6 → Converted to 3
  - `true` + `mostly-true` → **REAL**
  - `false` + `barely-true` + `pants-fire` → **FAKE**
  - `half-true` → **NOT_ENOUGH_INFO**

**Data Split:**
- Train: 10,269 samples
- Test: 1,284 samples
- Validation: 1,283 samples

## 🔧 Key Features

### Data Preprocessing
- URL removal
- HTML tag removal
- Special character removal
- Lowercase conversion
- Whitespace normalization
- Label conversion (6 → 3 classes)

### Models
1. **Semantic Similarity Model**
   - Matches claims with evidence
   - Uses sentence embeddings
   
2. **NLI Model**
   - Classifies claim-evidence pairs
   - Outputs: REAL / FAKE / NOT_ENOUGH_INFO

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 📖 Usage Example

```python
from src.data_loader import DataLoader
from src.preprocessor import TextPreprocessor

# Load data
loader = DataLoader()
train_df, test_df, val_df = loader.load_preprocessed_data()

# Preprocess new text
text = "Some claim text"
clean_text = TextPreprocessor.clean_text(text)
print(clean_text)
```

## 🔗 Integration with Backend

The trained models will be exported as:
- **Semantic Model**: `models/semantic_model.pth`
- **NLI Model**: `models/nli_model.pth`
- **Tokenizer**: `models/tokenizer.pkl`

Backend team will:
1. Load these models
2. Accept claims from frontend
3. Run through full pipeline
4. Return: Verdict + Confidence + Evidence

## 📝 Next Steps

- [ ] Complete Notebook 01 - Data Exploration
- [ ] Complete Notebook 02 - Data Preprocessing
- [ ] Complete Notebook 03 - Feature Extraction
- [ ] Train Semantic Similarity Model
- [ ] Train NLI Model
- [ ] Evaluate Models
- [ ] Test Full Pipeline

## ⚠️ Important Notes

- Run notebooks in **Google Colab** for GPU acceleration
- Upload Kaggle API token before running download
- Adjust batch size based on GPU memory
- Models will be saved automatically after training

## 📫 Contact

**ML Person**: Niranjan S
- Handles: Data preparation, model training, evaluation

**Backend Person**: [TBD]
- Handles: Server setup, model integration

**Frontend Person**: [TBD]
- Handles: UI/UX, user input handling

---
**Version**: 1.0  
**Last Updated**: February 2026
