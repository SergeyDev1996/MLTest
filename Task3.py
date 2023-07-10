import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the database
data = pd.read_csv("HR.csv")

# Step 2: Data Exploration and Preprocessing (if required)
# Assuming the data doesn't require extensive preprocessing for this example

# Step 3: Feature Selection and Engineering
# Select relevant features for prediction
features = ['satisfaction_level', 'last_evaluation', 'number_project',
            'average_montly_hours', 'time_spend_company', 'Work_accident',
            'promotion_last_5years', 'sales', 'salary']

# Convert categorical variables to numerical using one-hot encoding
data_encoded = pd.get_dummies(data[features])

# Extract the target variable (employees who left the company)
target = data['left']
employee_working = target.value_counts()[0]
employee_left = target.value_counts()[1]


# Step 4: Split the Data
X_train, X_test, y_train, y_test = train_test_split(data_encoded, target,
                                                    test_size=0.2,
                                                    random_state=42)

# Step 5: Select and Train a Predictive Model
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Step 6: Model Evaluation and Feature Importance
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Get the coefficients of the model (importance of each feature)
coefficients = model.coef_[0]
feature_importance = dict(zip(data_encoded.columns, coefficients))
sorted_importance = sorted(feature_importance.items(),
                           key=lambda x: abs(x[1]), reverse=True)

# Print the feature importance
most_important_feature = sorted_importance[0][0]
importance_score = sorted_importance[0][1]

# Step 7: Predicting Employees Who May Leave
# Assuming you want to predict on the entire dataset
data_encoded_scaled = scaler.transform(data_encoded)
predictions = model.predict(data_encoded_scaled)
data['predicted_left'] = predictions
predicted_counts = data['predicted_left'].value_counts()
employees_to_leave = predicted_counts[1]
print("Number of employees predicted to leave:", employees_to_leave)
print(f"We have {employee_working} working employees.")
print(f"We have {employee_left} employee that left.")
print("Most Important Feature:", most_important_feature)
print("Importance Score:", importance_score)
