# IDX_Summer_26_project
IDX Exchannge Data Science Internship 2026 California Property Close Price Prediction Model

# Project Overview
THis repository contains work completed during the internship involving anallysis of CRMLS data. The objective is to explore the dataset and prepare it for machine learning models that predict residential property sale proces. The tagrget variable is ClosePrice.

# Structure of the Repository
```text
IDX_Summer_26_project/
│
├── README.md
├──  Data_Science_v4.pdf
├── data/
│   └── data_dictionary.md
|   └── train_cleaned.csv
|   └── test_cleaned.csv
├── notebooks/
│   └── notebook01_exploration.ipynb
|   └── 02_preprocessing.ipynb
|   └── 03_baseline_model.ipynb
|   └── 04_model_comparison.ipynb
└── .gitignore
```

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

 # Week 3
 - Removed columns containing 100% of missing values
 - Removed variables where there is more than 50% missing data
 - Data Type Conversion:
    - Converted date-related columns to datetime format
    - converted PostalCode to string type
    - Boolean columns converted to binary integer
    - Drop columns with one unique value
  - Applied one-hot encoding to categorical columns, columns with more than 15 unique variables dropped
  - Normalization applied to the data to prevent skewing in linear regression and future ML models
  - Created Test/train split of the data
  - Exported cleaned CSV's of test/train splits

# Week 4
- Removed the upper 99.5th percentile of properties in ClosePrice due to swewing
- Hard coded City and PostalCode to be included in one hot encoding due to issues with linear regression
- Updated the test/train split to include the function format as a variable of X months
- Created X and Y for the linear regression, removed: CloseDate, ListPrice, OriginalListPrice, LisstingKey, ListingKeyNumeric, DaysOnMarket, and HighSchoolDistrict to prevent data leakages and remove data that would only be known after closing
- performed linear regression on X and Y using sklearn
- Evaluated R^2 on the linear regression and presented baseline results

# Week 5
- Completed Random Forest and Decision Tree fitting to the dataset
- Compared the metrics of Random Forest, Decision Tree, and Linear Regression
- Made a plot of the three methods referenced above
- Found the top 20 most important features out of the data
- Updated data test/train split to 30 months to match group goals
- Created a function to return metrics:R^2, RMSE, MAE, MAPE, and MdAPE

# Software
- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikitlearn
- Jupyter Lab/Jupyter Notebook
