import streamlit as st
import joblib

# Load các mô hình đã lưu
model_LinearRegression = joblib.load('weights/linear_regression_model.pkl')
model_RandomForestRegressor = joblib.load('weights/random_forest_model.pkl')
model_GradientBoostingRegressor = joblib.load('weights/gradient_boosting_model.pkl')
model_KNeighborsRegressor = joblib.load('weights/knn_model.pkl')

# Ánh xạ khu vực và loại bất động sản
khu_vuc_mapping = {
    0: 'Ba Vì', 1: 'Ba Đình', 2: 'Bắc Từ Liêm', 3: 'Chương Mỹ', 4: 'Cầu Giấy', 5: 'Gia Lâm', 6: 'Hai Bà Trưng',
    7: 'Hoài Đức', 8: 'Hoàn Kiếm', 9: 'Hoàng Mai', 10: 'Hà Đông', 11: 'Long Biên', 12: 'Mê Linh', 13: 'Mỹ Đức',
    14: 'Nam Từ Liêm', 15: 'Phú Xuyên', 16: 'Phúc Thọ', 17: 'Quốc Oai', 18: 'Sóc Sơn', 19: 'Sơn Tây', 20: 'Thanh Oai',
    21: 'Thanh Trì', 22: 'Thanh Xuân', 23: 'Thường Tín', 24: 'Thạch Thất', 25: 'Tây Hồ', 26: 'Đan Phượng', 27: 'Đông Anh',
    28: 'Đống Đa', 29: 'Ứng Hòa'
}

loai_bds_mapping = {
    0: 'Bán đất', 
    1: 'Chung cư mini, căn hộ dịch vụ', 
    2: 'Căn hộ chung cư', 
    3: 'Kho, nhà xưởng', 
    4: 'Loại bất động sản khác',
    5: 'Nhà biệt thự, liền kề', 
    6: 'Nhà mặt phố', 
    7: 'Nhà riêng', 
    8: 'Shophouse, nhà phố thương mại', 
    9: 'Trang trại, khu nghỉ dưỡng',
    10: 'Đất nền dự án'
}

st.title('Dự đoán giá trị bất động sản')

# Nhập các thông tin liên quan
area = st.number_input('Nhập diện tích (m²)', min_value=1.0, max_value=10000.0, value=100.0)
frontage = st.number_input('Nhập mặt tiền (m)', min_value=1.0, max_value=100.0, value=5.0)
num_floors = st.number_input('Nhập số tầng', min_value=1, max_value=10, value=1)
num_bedrooms = st.number_input('Nhập số phòng ngủ', min_value=1, max_value=20, value=2)
num_toilets = st.number_input('Nhập số toilet', min_value=1, max_value=10, value=1)

# Chọn khu vực và loại bất động sản
selected_khu_vuc = st.selectbox('Chọn khu vực', list(khu_vuc_mapping.values()))
selected_loai_bds = st.selectbox('Chọn loại bất động sản', list(loai_bds_mapping.values()))

# Chọn mô hình dự đoán
model_names = st.selectbox(
    'Chọn mô hình để dự đoán:',
    ['KNeighborsRegressor', 'GradientBoostingRegressor', 'RandomForestRegressor', 'LinearRegression']
)

# Tìm giá trị ánh xạ tương ứng với khu vực và loại bất động sản đã chọn
selected_khu_vuc_value = [key for key, value in khu_vuc_mapping.items() if value == selected_khu_vuc][0]
selected_loai_bds_value = [key for key, value in loai_bds_mapping.items() if value == selected_loai_bds][0]

# Map mô hình dự đoán
model_options = {
    'KNeighborsRegressor': model_KNeighborsRegressor,
    'GradientBoostingRegressor': model_GradientBoostingRegressor,
    'RandomForestRegressor': model_RandomForestRegressor,
    'LinearRegression': model_LinearRegression
}

# Khi người dùng nhấn nút để tính toán giá nhà
if st.button('Tính toán giá nhà'):
    # Tạo dữ liệu đầu vào cho mô hình
    input_data = [[area, frontage, num_floors, selected_khu_vuc_value, selected_loai_bds_value, num_bedrooms, num_toilets]]
    
    # Dự đoán giá trị bất động sản
    price_pred = model_options[model_names].predict(input_data)

    # Hiển thị kết quả dự đoán
    st.write(f'Dự đoán giá trị bất động sản bằng mô hình {model_names} là: {price_pred[0]:,.3f}')
