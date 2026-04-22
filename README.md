# 🏡 Airbnb Price Prediction & Data Analysis

An end-to-end **Data Science & Machine Learning** project that analyzes Airbnb listings and predicts prices using multiple supervised regression models.

## 🚀 Project Highlights
- 📊 Performed comprehensive EDA to uncover patterns in Airbnb listings
- 🧹 Applied data cleaning & preprocessing techniques
- ⚙️ Implemented feature engineering (FE) for better model performance
- 🤖 Trained and compared 7 regression models
- 📈 Built visualizations for data storytelling & insights

## 📁 Dataset
The dataset is sourced from Kaggle:
🔗 [Airbnb Open Data](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata)

**📌 Dataset Features:**
- Location (neighbourhood, latitude, longitude)
- Room type
- Price
- Availability
- Reviews & ratings
- Host-related information

## 🧹 Data Cleaning

**Steps performed:**
- Handling missing values (null imputation / removal)
- Removing duplicates
- Converting price to numeric format
- Fixing inconsistent categorical values
- Outlier detection & treatment

## 📊 Exploratory Data Analysis (EDA)

**Key analyses:**
- Price distribution across locations
- Room type vs price comparison
- Availability trends
- Correlation between features
- Impact of reviews on pricing

## ⚙️ Feature Engineering
- Extracted meaningful features from raw data
- Encoded categorical variables (Label / One-hot encoding)
- Feature scaling (Standardization / Normalization)
- Created derived variables for better predictions

## 🤖 Machine Learning Models

The following supervised regression models were implemented and compared:
1. Linear Regression
2. Support Vector Regression (SVR)
3. Decision Tree Regressor
4. Random Forest Regressor
5. AdaBoost Regressor
6. Gradient Boosting Regressor
7. XGBoost Regressor

## ⚡ Hyperparameter Tuning

- Applied **GridSearchCV** for exhaustive parameter tuning  
- Used **RandomizedSearchCV** for efficient hyperparameter optimization  
- Improved model performance by selecting optimal parameter combinations  

## 📈 Model Evaluation

Evaluation metrics used:
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

✔️ Models were further optimized using:
- GridSearchCV  
- RandomizedSearchCV  

## 📊 Visualizations
- 📉 Price distribution plots
- 📍 Location-based analysis
- 📊 Feature correlation heatmaps
- 📈 Model performance comparison graphs

## 🛠️ Tech Stack
- Python 🐍
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost
