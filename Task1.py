import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
dataset = pd.read_csv("IceCreamData.csv")
# Display the first few rows of the dataset
X = dataset['Temperature'].values.reshape(-1, 1)
y = dataset['Revenue'].values

# We need to train the model!0
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create an instance of the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Predict the revenue for a new temperature value
new_temperature = [[25]]  # Example input value
predicted_revenue = model.predict(new_temperature)
print(f"Predicted revenue: {predicted_revenue}")
