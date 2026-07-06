# IDX_Summer_26_project
IDX Exchannge Data Science Internship 2026 California Property Close Price Prediction Model

# Project Overview
THis repository contains work completed during the internship involving anallysis of CRMLS data. The objective is to explore the dataset and prepare it for machine learning models that predict residential property sale proces. The tagrget variable is ClosePrice.

# Structure of the Repository
IDX_Summer_26_project/
│
├── README.md                  # Project overview
├── report/
│   └── Data_Science_v4.pdf    
│
├── data/
│   └── data_dictionary.md      # Description of variables
│
├── notebooks/
│   └── notebook01_exploration.ipynb    # Jupyter notebook(s)
│
│
├── .gitignore

# Dataset
The analysis was performed using 24 months of CRMLS Sold property data, restricted to single family homes.

# Week 1
- Created github
- Downloaded project data
- Reviewed the CRMLS metedata documentation
- Documented the structure and purpose of key columns within the dataset

# Week 2
- Loaded CRMLS data into pandas into a jupyter notebook
- Filtered records to:
  - PropertyType = Residential
  - PropertySubType = SingleFamilyResidence
- Performed exploratory data analysis (EDA) on:
  - ClosePrice
  - LivingArea
  - BedroomsTotal
  - BathroomsTotalInteger
  - LotSizeArea
 

# Software
- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikitlearn
- Jupyter Lab/Jupyter Notebook
