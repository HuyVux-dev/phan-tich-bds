import streamlit as st
import joblib

model_LinearRegression = joblib.load('weights/linear_regression_model.pkl')
model_RandomForestRegressor = joblib.load('weights/random_forest_model.pkl')
model_GradientBoostingRegressor = joblib.load('weights/gradient_boosting_model.pkl')
model_KNeighborsRegressor = joblib.load('weights/knn_model.pkl')

st.title('Dự đoán giá trị bất động sản')

area = st.number_input('Nhập diện tích (m²)', min_value=1.0, max_value=10000.0, value=100.0)
frontage = st.number_input('Nhập mặt tiền (m)', min_value=1.0, max_value=100.0, value=5.0)
num_floors = st.number_input('Nhập số tầng', min_value=1, max_value=10, value=1)
num_bedrooms = st.number_input('Nhập số phòng ngủ', min_value=1, max_value=20, value=2)
num_toilets = st.number_input('Nhập số toilet', min_value=1, max_value=10, value=1)

model_names = st.selectbox(
    'Chọn mô hình để dự đoán:',
    ['KNeighborsRegressor', 'GradientBoostingRegressor', 'RandomForestRegressor', 'LinearRegression']
)

model_options = {
    'KNeighborsRegressor': model_KNeighborsRegressor,
    'GradientBoostingRegressor': model_GradientBoostingRegressor,
    'RandomForestRegressor': model_RandomForestRegressor,
    'LinearRegression': model_LinearRegression
}

if st.button('Tính toán gia nha:'):
    input_data = [[area, frontage, num_floors, num_bedrooms, num_toilets]]
    price_pred = model_options[model_names].predict(input_data)

    st.write(f'Dự đoán giá trị bất động sản bằng mô hình {model_names} là: {price_pred[0]:,.3f}')

