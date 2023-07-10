import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def load_dataset(filename):
    return pd.read_csv(filename)


def train_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def predict_revenue(model, new_temperature):
    return model.predict([[new_temperature]])


if __name__ == "__main__":
    dataset = load_dataset("IceCreamData.csv")
    X = dataset['Temperature'].values.reshape(-1, 1)
    y = dataset['Revenue'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42)

    model = train_linear_regression(X_train, y_train)

    mse, r2 = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    new_temperature = 25  # Example input value
    predicted_revenue = predict_revenue(model, new_temperature)
    print(f"Predicted revenue: {predicted_revenue}")
