# Predicting and Understanding Health Outcomes: A Causal Analysis Of Healthcare Surveys

This repository supports the ML808 project, which analyzes the relationships between lifestyle factors and chronic diseases using predictive models and causal inference techniques. We work with **NHANES (2021–2023)** data to predict and explain outcomes for **Diabetes**, **Cardiovascular Disease (CVD)**, and **Kidney Disease**.

---

## 📁 Repository Structure

---
├── demographic/ # Raw demographic CSVs or preprocess scripts 

├── diet/ # Dietary survey data 

├── examination/ # Physical examination data 

├── laboratory/ # Blood/urine biomarker data 

├── questionnaire/ # Self-reported condition data 

├── saved_models/ # Trained ML models (e.g., .pkl) 

├── NHANES_FULL.csv # Full preprocessed dataset 

├── NHANES_SAMPLE.csv # Smaller working sample 

├── diabetes.csv # Domain-based features for diabetes modeling 

├── cvd.csv # Domain-based features for cardiovascular modeling 

├── kidney_disease.csv # Final features for kidney modeling 

├── feature_sets_*.pkl # Selected features from LASSO, corr, etc. 

├── predictive.ipynb # Model training & evaluation 

├── causal_algorithms.ipynb # Causal structure learning (PC, GES, LiNGAM) 

├── features.ipynb # Feature selection and overlap analysis 

├── environment_ml808.yml # Conda environment config 

├── requirements.txt # Python dependencies
---

## 🚀 How to Run

### 1. Set Up Environment

```bash
conda env create -f environment_ml808.yml
conda activate ml808
```
OR

```
pip install -r requirements.txt
```

## 📎 Resources

- 📘 [NHANES]([https://www.cdc.gov/nchs/nhanes/index.htm](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023))

---

## ✍️ Author

**Maiya Goloburda**  
[maiya.goloburda@mbzuai.ac.ae](mailto:maiya.goloburda@mbzuai.ac.ae)
