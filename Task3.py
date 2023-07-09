import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

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
param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [None, 5, 10]}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)
model = grid_search.best_estimator_

# Step 5: Identify the feature contributing the most
feature_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
most_contributing_feature = feature_importance.index[0]
print(f"The feature contributing the most is: {most_contributing_feature}")

# Step 6: Predicting employees who may leave the company
y_pred = model.predict(X_test)
predicted_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predicted_df)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"Confusion Matrix:\n{confusion_mat}")

# Additional evaluation using cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean Cross-Validation Score: {cv_scores.mean()}")
