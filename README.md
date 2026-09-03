# IDX_Summer_26_project
IDX Exchannge Data Science Internship 2026 California Property Close Price Prediction Model

# Project Overview
This repository contains work completed during the internship involving anallysis of CRMLS data. The objective is to explore the dataset and prepare it for machine learning models that predict residential property sale proces. The tagrget variable is ClosePrice.

# Structure of the Repository
```text
IDX_Summer_26_project/
│
├── README.md
├── Data_Science_v4.pdf
├── app.py
├── data/
│   └── data_dictionary.md
|   └── train_cleaned.csv
|   └── test_cleaned.csv
├── notebooks/
│   └── 01_exploration.ipynb
|   └── 02_preprocessing.ipynb
|   └── 03_baseline_model.ipynb
|   └── 04_model_comparison.ipynb
|   └── 05_advanced_models.ipynb
|   └── 06_evaluation.ipynb
└── .gitignore
```

# Dataset
- **Source:** California Regional Multiple Listing Service (CRMLS) accessed via FTP through IDX Exchange
- **Coverage:** January 2022 – June 2026 (31 monthly CSV files)
- **Size:** 400,000+ raw records, filtered to 328,000+ single-family residential properties
- **Target Variable:** ClosePrice (residential sale price in USD)
- **Filter:** PropertyType = Residential, PropertySubType = SingleFamilyResidence
- **Note:** Raw data files are not tracked in this repository due to size. Contact IDX Exchange for data access.

# Preprocessing Steps
The following steps were applied in "02_preprocessing.ipynb":
1. **Filtering** — Restricted to single-family residential properties
2. **Missing Value Handling** — Removed columns with 100% missing values, removed columns with more than 50% missing data, imputed remaining numeric columns with median and categorical columns with mode
3. **Data Type Conversion** — Converted date columns to datetime, PostalCode to string, boolean columns to binary integer, and integer-like features to Int64
4. **Outlier Removal** — Removed logical impossibilities (zero square footage, impossible bedroom counts), removed duplicate transactions, and applied price/sqft filter to catch data entry errors
5. **Outlier Thresholds** — Computed from training data only (0.5th and 99.5th percentile) and applied as frozen cutoffs to both train and test sets to prevent leakage
6. **Encoding** — Applied one-hot encoding to low-cardinality categorical columns, label encoded school district names
7. **Feature Engineering** — Added BedBathRatio, PropertyAge, AreaPerBedroom, and school district geographic layer via spatial join with California Unified School District boundaries using GeoPandas
8. **Normalization** — Applied StandardScaler to continuous numeric features
9. **Train/Validation/Test Split** — Chronological time-based split: training (30 months), validation (second most recent month), test (most recent month — June 2026)

# Model Descriptions
Five model types were trained and compared across Weeks 4-7:
- **Linear Regression** (`03_baseline_model.ipynb`) — Baseline model assuming linear relationships between features and price. Fast and interpretable but limited in capturing complex pricing patterns.
- **Decision Tree** (`04_model_comparison.ipynb`) — Captures non-linear relationships by splitting data into branches. Prone to overfitting; controlled via max_depth parameter.
- **Random Forest** (`04_model_comparison.ipynb`) — Ensemble of 100 decision trees trained on random subsets of data and features. Much more robust to overfitting than a single tree. Best Random Forest MdAPE: 7.95%.
- **LightGBM** (`05_advanced_models.ipynb`) — Gradient boosting model optimized for speed and large datasets. Tuned using manual hyperparameter search with early stopping on validation set. Best LightGBM MdAPE: 8.21%.
- **XGBoost** (`05_advanced_models.ipynb`) — Gradient boosting model with sequential tree building. Final model selected after systematic hyperparameter tuning across depth, learning rate, subsample, and colsample parameters using chronological validation set for early stopping.

# Best Evaluation Results
Final model: **XGBoost** (max_depth=11, learning_rate=0.05, subsample=0.9, colsample_bytree=0.8)

| Model | R² | RMSE | MAE | MAPE | MdAPE |
|---|---|---|---|---|---|
| Linear Regression | 0.4787 | $653,574 | $436,431 | 43.73% | 30.42% |
| Decision Tree | 0.7814 | $423,219 | $242,696 | 19.73% | 13.87% |
| Random Forest | 0.8806 | $312,748 | $167,504 | 13.20% | 8.95% |
| Random Forest (engineered) | 0.8920 | $297,504 | $154,714 | 11.98% | 7.95% |
| LightGBM (tuned) | 0.9078 | $274,801 | $148,945 | 11.84% | 8.21% |
| XGBoost (tuned) | 0.9070 | $279,826 | $147,190 | 11.19% | **7.66%** |

**Performance by Price Band (XGBoost):**
- Mid ($500k–$750k): MdAPE 6.29%
- Upper Mid ($750k–$1M): MdAPE 6.58%
- Entry (<$500k): MdAPE 8.00%
- Luxury ($1M–$2M): MdAPE 8.62%
- Ultra Luxury (>$2M): MdAPE 11.25%

# Instructions for Rerunning the Project
Run the notebooks in order from your terminal or Jupyter Lab:

1. **Download data** from CRMLS via FTP and save monthly CSV files to your local data folder
2. **Run `notebook01_exploration.ipynb`** — exploratory data analysis and data dictionary
3. **Run `02_preprocessing.ipynb`** — data cleaning, feature engineering, and train/val/test split. Exports `train_enriched.csv` and `test_enriched.csv`
4. **Run `03_baseline_model.ipynb`** — trains and evaluates Linear Regression baseline
5. **Run `04_model_comparison.ipynb`** — trains Decision Tree and Random Forest, compares all models
6. **Run `05_advanced_models.ipynb`** — trains LightGBM and XGBoost with hyperparameter tuning, saves final model
7. **Run `06_evaluation.ipynb`** — full evaluation including price band and geographic analysis, exports metrics_summary.csv

**Requirements:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn lightgbm xgboost geopandas streamlit joblib
```

**File paths:** Update the `filepath` variable at the top of each notebook to point to your local data directory.
# Instructions for Launching the Streamlit Application
The app requires the trained model files saved during Week 9. If not already saved, run `05_advanced_models.ipynb` through to the joblib export cells first.

**Install Streamlit if not already installed:**
```bash
pip install streamlit
```

**Navigate to the project folder and run:**
```bash
cd path/to/IDX_summer_internship
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

**Inputs:**
- Living Area (sq ft)
- Bedrooms
- Bathrooms
- Lot Size (sq ft)
- City (used for geographic coordinates)

**Output:** Estimated home sale price with a confidence range based on model MdAPE of 7.66%.


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

# Week 6
This week focuses on expanding the feature set used in the baseline models through two types of feature engineering: derived property features and a geographic school district layer.
- New Derived Featrues:
  - BedBathRatio - ratio of bedrooms to bathrooms
  - PropertyAge - age of the property at the time of sale (2026 minus Yearbuilt)
  - AreaPerBedroom - living area divided by number of bedrooms
- School District Layer:
  - California Unified School District boundaries were downloaded and spatially joined to each property using its latitude and longitude coordinates.
  - DistrictName was label encoded into DistictEncoded
- Results: the random forest R^2 was improved from 0.8806 to 0.8818 (previous to hyper parameter tuning)

# Week 7
- Implemented LIghtGBM and XGBoost gradient boosting models as an advanced alternative to Random Forest
- Performed light hyperparameter tuning on both models including n_estimators, max_depth, learning_rate, num_leaves, subsample, and colsample_bytree
- Introduced a three way split of data to introduce a validation set
    - Training set: 30 months of historical data
    - Validation set: second most recent month (April 2026)
    - Test set: most recent month (June 2026) used only once for final evaluation
- Used early stopping on the validation set to determine optimal number of trees without overfitting
- Removed non-California properties from training data
- Final model comparison across all weeks documented in 05_advanced_models.ipynb

# Week 8
- Created a dedicated evaluation notebook (06_evaluation.ipynb) to analyze model performance beyond top-line metrics
- Computed full suite of evaluation metrics: R², RMSE, MAE, MAPE, and MdAPE on the final XGBoost model
- Analyzed model performance by price band using California market-appropriate segments:
  - Entry (<$500k), Mid ($500k-$750k), Upper Mid ($750k-$1M), Luxury ($1M-$2M), Ultra Luxury (>$2M)
  - Model performs best on mid-market properties (MdAPE 6.29-6.58%) and struggles most on ultra luxury (MdAPE 11.25%)
- Analyzed model performance by unified school district to identify geographic areas of underperformance
- Generated evaluation plots including:
  - MdAPE by price band bar chart
  - Test set distribution by price band
  - Predicted vs actual scatter plot colored by prediction error
  - Over/underestimate breakdown by price band
- Exported metrics_summary.csv containing all model results across Weeks 4-7
- Documented key model limitations including scaled coordinates, ultra luxury underperformance, and market condition sensitivity

# Week 9
- Built an interactive Streamlit web application (`app.py`) for real-time California home price prediction
- App accepts four user inputs as specified: Living Area (sq ft), Bedrooms, Bathrooms, and Lot Size (sq ft)
- Added city dropdown to incorporate geographic location into predictions via scaled latitude and longitude coordinates
- Loaded trained XGBoost model, feature names, and feature medians using joblib
- All features not provided by the user are set to their training data median values to ensure realistic predictions
- Engineered features (BedBathRatio, AreaPerBedroom) are computed directly from user inputs at prediction time
- Displays estimated home value, property summary, and a confidence range based on the model MdAPE of 7.66%
- App runs locally via `streamlit run app.py`

# Week 10
- Updated README.md with full project documentation including dataset source, preprocessing steps, model descriptions, best evaluation results, and instructions for rerunning the project and launching the Streamlit application


# Software
- Python
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- LightGBM
- XGBoost
- GeoPandas
- Streamlit
- joblib
- Jupyter Lab / Jupyter Notebook
