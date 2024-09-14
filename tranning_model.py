from pandas import read_csv
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = read_csv('cleaned_data.csv')
X = df[['Diện tích',
 'Mặt tiền',
 'Số tầng',
 'Số phòng ngủ',
 'Số toilet']]
y = df['Mức giá']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_save_LinearRegression(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2_score = model.score(X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2_score}")
    print('#' * 50)
    
    joblib.dump(model, 'weights/linear_regression_model.pkl')
    print("SAVE linear_regression_model")

def train_and_save_RandomForestRegressor(X_train, X_test, y_train, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2_score = model.score(X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2_score}")
    print('#' * 50)
    
    joblib.dump(model, 'weights/random_forest_model.pkl')
    print("SAVE random_forest_model")
    
def train_and_save_GradientBoostingRegressor(X_train, X_test, y_train, y_test):
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2_score = model.score(X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2_score}")
    print('#' * 50)
    
    joblib.dump(model, 'weights/gradient_boosting_model.pkl')
    print("SAVE gradient_boosting_model")
    
    
def train_and_save_KNeighborsRegressor(X_train, X_test, y_train, y_test):
    model = KNeighborsRegressor(n_neighbors=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2_score = model.score(X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2_score}")
    print('#' * 50)

    joblib.dump(model, 'weights/knn_model.pkl')
    print("SAVE gradient_bknn_modeloosting_model")
    

def main():
    train_and_save_LinearRegression(X_train, X_test, y_train, y_test)
    train_and_save_RandomForestRegressor(X_train, X_test, y_train, y_test)
    train_and_save_GradientBoostingRegressor(X_train, X_test, y_train, y_test)
    train_and_save_KNeighborsRegressor(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()