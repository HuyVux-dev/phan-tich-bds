from pandas import read_csv
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = read_csv('cleaned_data.csv')
X = df[['dien_tich', 'so_phong', 'nam_xay_dung']]
y = df['gia']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_save_LinearRegression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # Tính MSE
    mse = mean_squared_error(y_test, y_pred)
    # Tính R-squared
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse}")
    print(f"R-squared: {r2}")
    print('#' * 50)
    joblib.dump(model, 'linear_regression_model.pkl')
    print("SAVE linear_regression_model")

def train_and_save_LinearRegression(X_train, y_train):

