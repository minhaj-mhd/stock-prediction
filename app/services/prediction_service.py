from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow.keras.models import load_model
import os

model = load_model(os.path.join(os.path.dirname(__file__), "../models/stock_model.h5"))


def get_prediction(df, ticker):
    scaled_data, scaler = preprocess_data(df)
    # Dummy prediction logic
    last_price = scaled_data[-1][0]
    prediction = last_price * 1.01
    return scaler.inverse_transform([[prediction]])[0][0]

def preprocess_data(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['Close']])
    return scaled_data, scaler