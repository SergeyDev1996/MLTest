import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Load and preprocess the data

df = pd.read_csv("HR.csv")

# Step 2: Feature selection and engineering
# Assuming the 'left' column is the target indicator
features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
            'time_spend_company', 'Work_accident', 'promotion_last_5years']
target = 'left'

# One-hot encode the 'sales' and 'salary' columns
df_encoded = pd.get_dummies(df, columns=['sales', 'salary'], drop_first=True)

# Preprocess the data if needed (e.g., handle missing values)

# Step 3: Split the data into training and testing sets
X = df_encoded[features]
y = df_encoded[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train and evaluate prediction models
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Identify the technology contributing the most
feature_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
most_contributing_technology = feature_importance.index[0]
print(f"The technology contributing the most is: {most_contributing_technology}")

# Step 6: Predicting employees who may leave the company
y_pred = model.predict(X_test)
predicted_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predicted_df)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_mat}")
