import pickle
import numpy as np
import tensorflow as tf
import pandas as pd 
from sklearn.preprocessing import StandardScaler

class Dudoangiaxe:
    def __init__(self):  
        self.model_path = "models/car_price_model.h5"  
        self.scaler_x_path = "models/scaler_x.pkl"
        self.scaler_y_path = "models/scaler_y.pkl"
        self.columns_path = "models/x_encoded_columns.pkl"
        self.model = tf.keras.models.load_model(self.model_path, compile=False) #load model đã được huấn luyện
        #load scaler x để chuẩn hóa đầu vào
        with open(self.scaler_x_path,"rb") as f:
            self.scaler_x=pickle.load(f)
    
        #load scaler y để chuẩn hóa đầu vào
        with open('models/scaler_y.pkl',"rb") as f:
            self.scaler_y=pickle.load(f)

        #load danh sách cột đã mã hóa
        with open(self.columns_path,"rb") as f:
            self.x_columns=pickle.load(f)
    
    def preprocess_input(self,data):
        #chuyển dữ liệu đầu vào thành dataframe
        df=pd.DataFrame([data])
        #chuyển dữ liệu dạng chữ thành số
        df_encoded=pd.get_dummies(df)
        #đảm bảo dữ liệu có đủ các cột cần thiết (nếu thiếu điền 0)
        df_encoded=df_encoded.reindex(columns=self.x_columns,fill_value=0)

        #chuẩn hóa dữ liệu bằng scaler x
        chuanhoa_x_scaler=self.scaler_x.transform(df_encoded)
        return chuanhoa_x_scaler
        
    def predict_price(self,data): #dự đoán giá xe từ dữ liệu đầu vào
        x_scaled=self.preprocess_input(data) #tiền xử l1y dữ liệu
        #dự đoán giá xe (được chuẩn hóa)
        giaxe_scaled=self.model.predict(x_scaled)
        #chuyển giá trị dự đoán về thang do gốc bằng scaler y
        ketqua=self.scaler_y.inverse_transform(giaxe_scaled)
        return round(ketqua[0][0],0) # trả về kết quả cuối cùng , làm tròn