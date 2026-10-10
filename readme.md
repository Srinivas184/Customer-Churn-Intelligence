# Customer Intelligence & Churn Prediction System

## About the Project

Why do some customers stay with a company for years while others leave after just a few months?

I built this project to explore that question using machine learning and data analytics. The goal was to predict which customers are more likely to leave, understand the patterns behind customer churn, and identify customers who may benefit from retention efforts.

I worked with the IBM Telco Customer Churn dataset and built an end-to-end workflow covering data analysis, machine learning, customer segmentation, SQL analytics, and an interactive Streamlit application.

## What I Built

- **Churn Prediction:** Estimated the probability of a customer leaving using machine learning.
- **Customer Segmentation:** Used K-Means clustering to group customers based on tenure, monthly charges, and total charges.
- **Model Explainability:** Used SHAP to understand which features influence the model's predictions.
- **Retention Recommendations:** Added simple business rules to suggest possible actions for customers at different risk levels.
- **SQL Analysis:** Explored churn patterns across contract types, payment methods, and customer segments.
- **Interactive App:** Built a Streamlit interface where users can enter customer details and view predictions.

## Tools & Technologies

- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn, XGBoost
- SHAP
- MySQL
- Streamlit
- Git and GitHub

## My Approach

I started by cleaning the dataset and exploring how churn relates to customer tenure, monthly charges, contract types, payment methods, and subscribed services.

After preparing the data, I trained and compared three classification models:

- Logistic Regression
- Random Forest
- XGBoost

I evaluated their performance using accuracy, precision, recall, F1-score, ROC-AUC, and five-fold cross-validation. I then used SHAP to explore the factors influencing predictions and K-Means to identify four broad customer segments.

Finally, I connected the saved model and preprocessing components to a Streamlit app so users can test different customer profiles without running the training notebook again.

## Model Results

Here is how the three models performed on my test dataset:

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 81.48% | 67.71% | 57.75% | 62.34% | 86.57% |
| Random Forest | 79.13% | 59.39% | 67.65% | 63.25% | 84.58% |
| XGBoost | 81.83% | 69.67% | 55.88% | 62.02% | 86.41% |

I selected Logistic Regression for the application because it offered strong overall discrimination and achieved a mean ROC-AUC of approximately 0.840 in five-fold cross-validation. Random Forest had better recall on the test set, which is also important when identifying customers who may churn.

These results come from my current experimental setup and may differ on new data.

## Customer Segmentation

I used K-Means clustering to group customers using three features: tenure, monthly charges, and total charges.

The four groups were interpreted as:

- **New / Low-Value**
- **Loyal / High-Value**
- **Newer / High-Spend**
- **Loyal / Low-Spend**

I also compared churn rates across these groups to understand how their behavior differed. These names describe the observed cluster profiles rather than verified measures of customer value.

## How the App Works

The Streamlit app allows a user to enter customer details and view:

- Estimated churn probability
- High, medium, or low risk category
- Customer segment
- Suggested retention action

The risk categories use thresholds defined for this project: high risk at 70% or above, medium risk from 40% to below 70%, and low risk below 40%.

The recommendations are rule-based suggestions, not guaranteed ways to prevent churn.

## Project Structure

```text
Customer_Churn_Intelligence/
├── app/
│   └── app.py
├── data/
├── models/
│   └── churn_artifacts.pkl
├── notebooks/
│   └── 01_data_understanding.ipynb
├── reports/
├── sql/
│   └── customer_churn_analysis.sql
├── requirements.txt
└── README.md
```

## Running the Project

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Customer_Churn_Intelligence
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual repository URL.

**2. Install the required packages**

```bash
python -m pip install -r requirements.txt
```

**3. Make sure the model artifacts are available**

The app needs `models/churn_artifacts.pkl`, which contains the trained model and preprocessing components. This file must be included in your local project or generated from the notebook.

**4. Start the application**

```bash
python -m streamlit run app/app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## What I Learned

While working on this project, I gained practical experience with data cleaning, exploratory data analysis, feature preprocessing, classification models, model evaluation, SHAP, clustering, SQL, and building a simple ML application with Streamlit.

It also helped me understand that a useful machine learning project involves more than training a model. The results need to be evaluated, interpreted, and presented in a way that helps people make better decisions.

## Future Improvements

There is still room to improve the project. Some ideas I would like to explore are probability calibration, better decision thresholds, batch predictions for multiple customers, model monitoring, and deploying the application online.

## Author

**Srinivas**

Interested in Machine Learning, Data Analytics, and building practical projects that turn data into useful insights.
